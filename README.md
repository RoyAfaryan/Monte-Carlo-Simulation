# Monte-Carlo-Simulation

## Description
This project estimates the value of Pi using the Monte Carlo method, implemented with both MPI and multithreading for parallel computation. The Monte Carlo method involves generating random points within a unit square and determining how many fall inside a quarter circle inscribed within that square. The ratio of points inside the quarter circle to the total points generated, multiplied by 4, approximates the value of Pi.

## MPI Implementation
Using MPI (Message Passing Interface), the computational workload is distributed across multiple processors. This parallel approach enhances efficiency and accuracy, allowing the program to handle a larger number of points.

## Multithreading Implementation
Using multithreading, the computational workload is divided across multiple threads within a single process. This also improves efficiency and accuracy by leveraging concurrent execution on multi-core processors.
