(* Michael Bartoli
 * Asgt07
 * cs52
 * Prof. Bull
 * 11/15/2012
 *)

Control.Print.stringDepth := 2000;

(* Problem 1 *)
(* our powermod function computes b^e mod m *)
fun powermod b e m = if compare e zero = EQUAL
                        then one
                     else if (rem e two) = zero
                         then rem (square (powermod b (quo e two) m)) m 
                     else rem (prod b (square (powermod b (quo e two) m))) m

(* Problem 2*)
(* block returns a cs52int list, and unblock returns a cs52int  *)
fun block n m = if (less m one) 
                then nil
                else (rem m n)::(block n (quo m n))

fun unblock n nil = zero
  | unblock n (m::mt) = sum m (prod n (unblock n mt))
                         

(* Problem 3*)
(* the following two functions switch the values *)
fun stringToCs52int string = unblock (fromInt 256) (map fromInt(map ord (explode string)))

fun Cs52IntToString csInt = implode (map chr (map toInt (block (fromInt 256) csInt)));


(* Problem 4*)

(* Problem 5*)
(* part a *)
(* The function encodeString takes a key (e,n) and a string, and produces a single
 * cs52int value that encrypts the message contained in the string *)

(* aux function to encodeString *)
fun rsaEncode (e,n) m = if (greatereq m n) then zero
                        else powermod m e n;

fun encodeString (e,n) string = 
    unblock n (map (rsaEncode (e,n)) (block n (stringToCs52int string)));

val a = fromInt 7;
val b = fromInt 111;
val str = "Don't panic and always carry your towel.";

val codified = encodeString (a, b) str; 

(* Aux function to decodeString *)
fun rsaDecode (d, n) c = if (greatereq c n) then zero
                          else powermod c d n;

fun decodeString (d,n) codedNum = 
    Cs52IntToString (unblock n (map(rsaDecode (d,n)) (block n codedNum)));


val c = fromInt 31;
val uncodedC = decodeString (c,b) codified;

(* Problem 6 *)

(*
 * 
 *)


val seed = (47,42);
val generator = Random.rand seed;

fun industrialPrime k =
   let
       val p = randomCs52Int k generator;
       fun test p 0 = true
         | test p n = 
           let
               val a = randomCs52Int k generator;
          in 
               if(less a p) 
               andalso (powermod a p p = a)
               andalso (gcd a p = one)
                   then test p (n-1) (* I have n = 20 so there will be 20 different a's *)
               else false
          end;
    in
       if(test p 20 = true) then p
       else industrialPrime k
    end;

(* Probelm 7 *)

fun newRSAKeys k =
    let
        val p = industrialPrime k
        val q = industrialPrime k
        val n = prod p q
        val phi = prod (diff p one) (diff q one)
        fun dgenerator x =
            let val d = randomCs52Int k generator 
            in
                if (lesseq x d) orelse (lesseq d zero)
                then dgenerator x
                else if unequal (gcd d phi) one
                then dgenerator x
                else
                d
            end
            val correctD = dgenerator n;
    in
        if isSome (inversemod correctD phi)
           then ((valOf(inversemod correctD phi), n), (correctD,n))
        else
           newRSAKeys k
    end;

(* Problem 8 *)
(* this is where I need to genereate a pair of 28-bit keys. Choose
 * a secret message, one or two sentences in good taste, and encrypt
 * it with your public key (as if someone were sending the message to you).
 * Make this asgt07.rsa 
 * this is submitted seperately
 *)

(* Problem 9 *)
(* part a *)
(* 22821*d = 1 mod 51940 => d=701 
 * therefore, the private key, n = (701, 52753) 
 * the factorizaitons are 71 and 743 
*)
fun factorization m n = if rem n m = zero 
                        then (m, (quo n m))
                        else if isOdd m then factorization (sum m two) n
                        else factorization (sum m one) n; 

fun findKey (e, n) =
    let
        val (p,q) = factorization two n;
        val phi = prod (diff p one) (diff q one);
    in
        (valOf (inversemod e phi), n)
    end;

(* part b *)
(* radix^144 longer but radix is 2 so our answer is 2^144 longer *)