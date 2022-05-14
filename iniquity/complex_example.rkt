#lang racket
(define (even? x)
    (if (zero? x)
        #t
        (odd? (sub1 x))))
(define (odd? x)
    (if (zero? x)
        #f
        (even? (sub1 x))))
(if (even? 5)
    (odd? 102)
    (odd? 101)
    )
;; should return true