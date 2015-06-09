#! /usr/bin/perl -w
    eval 'exec /usr/bin/perl -S $0 ${1+"$@"}'
        if 0; #$running_under_some_shell

use strict;
use File::Find ();

# Set the variable $File::Find::dont_use_nlink if you're using AFS,
# since AFS cheats.

# for the convenience of &wanted calls, including -eval statements:
use vars qw/*name *dir *prune/;
*name   = *File::Find::name;
*dir    = *File::Find::dir;
*prune  = *File::Find::prune;

sub wanted;
sub ls ();


my @rwx = qw(--- --x -w- -wx r-- r-x rw- rwx);
my @moname = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);

my (%uid, %user);
while (my ($name, $pw, $uid) = getpwent) {
    $user{$uid} = $name unless exists $user{$uid};
}

my (%gid, %group);
while (my ($name, $pw, $gid) = getgrent) {
    $group{$gid} = $name unless exists $group{$gid};
}


# Traverse desired filesystems
File::Find::find({wanted => \&wanted}, '/');
exit;


sub wanted {
    my ($dev,$ino,$mode,$nlink,$uid,$gid);

    /^.*\.pdf\z/s &&
    (($dev,$ino,$mode,$nlink,$uid,$gid) = lstat($_)) &&
    ls;
}


sub sizemm {
    my $rdev = shift;
    sprintf("%3d, %3d", ($rdev >> 8) & 0xff, $rdev & 0xff);
}

sub ls () {
    my ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,
        $atime,$mtime,$ctime,$blksize,$blocks) = lstat(_);
    my $pname = $name;

    $blocks
        or $blocks = int(($size + 1023) / 1024);

    my $perms = $rwx[$mode & 7];
    $mode >>= 3;
    $perms = $rwx[$mode & 7] . $perms;
    $mode >>= 3;
    $perms = $rwx[$mode & 7] . $perms;
    substr($perms, 2, 1) =~ tr/-x/Ss/ if -u _;
    substr($perms, 5, 1) =~ tr/-x/Ss/ if -g _;
    substr($perms, 8, 1) =~ tr/-x/Tt/ if -k _;
    if    (-f _) { $perms = '-' . $perms; }
    elsif (-d _) { $perms = 'd' . $perms; }
    elsif (-l _) { $perms = 'l' . $perms; $pname .= ' -> ' . readlink($_); }
    elsif (-c _) { $perms = 'c' . $perms; $size = sizemm($rdev); }
    elsif (-b _) { $perms = 'b' . $perms; $size = sizemm($rdev); }
    elsif (-p _) { $perms = 'p' . $perms; }
    elsif (-S _) { $perms = 's' . $perms; }
    else         { $perms = '?' . $perms; }

    my $user = $user{$uid} || $uid;
    my $group = $group{$gid} || $gid;

    my ($sec,$min,$hour,$mday,$mon,$timeyear) = localtime($mtime);
    if (-M _ > 365.25 / 2) {
        $timeyear += 1900;
    } else {
        $timeyear = sprintf("%02d:%02d", $hour, $min);
    }

    printf "%5lu %4ld %-10s %3d %-8s %-8s %8s %s %2d %5s %s\n",
            $ino,
                 $blocks,
                      $perms,
                            $nlink,
                                $user,
                                     $group,
                                          $size,
                                              $moname[$mon],
                                                 $mday,
                                                     $timeyear,
                                                         $pname;
    1;
}

