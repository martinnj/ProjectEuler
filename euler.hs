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
