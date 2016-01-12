{- Imports -}
import Data.Char
import Data.List

{- Problem 1 -}
{- Find the sum of all the multiples of 3 or 5 below 1000. -}
problem1list = [0..999]

-- Returns the value of the input is a multple of 3 or 5, otherwise 0.
mod3or5 :: Integer -> Integer
mod3or5 x = if ((x `mod` 3) == 0) || ((x `mod` 5) == 0)
            then x
            else 0

problem1 :: [Integer] -> Integer
problem1 xxs = foldr (+) 0 (map mod3or5 xxs)
problem1res = problem1 problem1list


{- Problem 2 -}
fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)
fibList = [fib x | x <- [0..34], ((fib x) `mod` 2) == 0]
problem2res = foldr (+) 0 fibList


{- Problem 3 -}
problem3input = 600851475143

-- No longer used.
isPrime :: Integer -> Bool
isPrime n
    | n <= 2 = False
    | n `mod` 2 == 0 = False
    | otherwise = not(foldr (||) False boolList)
        where  limit = round $ sqrt(fromIntegral n)
               ms = [3..limit]
               boolList = map (\x -> n `mod` x == 0) ms

-- Below solution is from https://wiki.haskell.org after
-- I had termination problems with my old one.
primes = 2 : filter (null . tail . primeFactors) [3,5..]

primeFactors :: Integer -> [Integer]
primeFactors n = factor n primes
  where
    factor n (p:ps)
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      =     factor n ps

problem3res = last (primeFactors problem3input)

{- Problem 4 -}
palindromes = [x | y <- [100..999], z <- [100..999], let x = y*z, (show x) == (reverse $ show x)]
problem4res = maximum palindromes


{- Problem 5 -}
evenly :: Integer -> [Integer] -> Bool
evenly 0 _ = False
evenly n [] = True
evenly n (x:xs) = (n `mod` x == 0) && evenly n xs

problem5res = head [x | x <- [0,20..], let ys = [1..20], evenly x ys]


{- Problem 6 -}
sumOfSquares = sum [x^2 | x <- [1..100]]
squareOfSums = (sum [1..100])^2
problem6res = abs $ sumOfSquares - squareOfSums

{- Problem 7 -}
-- Primes reused from problem 3.
problem7res = primes !! 10000

{- Problem 8 -}
thousandDigits = show 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
foo1' ns = if length(ns) >= 13
          then concat [[product $ (map digitToInt (take 13 $ ns))], foo1' $ tail ns]
          else [0]
problem8res = maximum $ foo1' thousandDigits

{- Problem 9 -}

triples d = [[a,b,c] | c <- [1..d], b <- [1..c], a <- [1..b], a^2+b^2==c^2, a+b+c==d]
problem9res = product $ head $ triples 1000

{- Problem 10 -}
problem10res = sum $ takeWhile (\x -> x < 2000000) primes

{- Problem 11 -}
-- TODO

{- Problem 12 -}
