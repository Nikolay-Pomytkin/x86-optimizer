#lang racket
(define (double x) (+ x x))
(let ([x 1])
    (let ([y 2])
        (let ([z (+ x y)])
            (double z)
        )
    )
)