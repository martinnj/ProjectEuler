{- Possible Imports -}


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