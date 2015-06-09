#!/usr/bin/perl -s

use Cwd;

sub ScanDirectory {
  my $workdir = shift;
  my $startdir = cwd;

  chdir $workdir or die "Unable to enter dir $workdir: $!\n";
  opendir my $DIR, '.' or die "Unable to read $workdir: $! \n";
  my @names = readdir $DIR or die "Unable to read current dir:$!\n";
  closedir $DIR;
  foreach my $name (@names) {
    next if ($name eq '.');
    next if ($name eq '..');
 
    if (-d $name) {
      ScanDirectory($name);
      next;
    }
    if ($name eq 'core') {
      if (define $r) {
        unlink $name or die "unable to delete $name: $!\n";
      } else {
        print "found one!\n";
      }
    }
  }
  chdir $startdir or die "unable to change dir $startdir: $!\n";
}

ScanDirectory('.');
