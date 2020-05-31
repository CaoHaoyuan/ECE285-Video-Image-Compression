# Overview
The code can be briefly divided to four parts:   
1. Unary encoder: If the number is n, the output is [1]*n + [0].   
2. Unary decoder: Just do the opposite thing as the encoder.  
3. Arithmetic encoder: I built a class so that the user can use encoder with whatever precision they want. In this case, I use 4 as required in the homework. The encoder operate in such way that floating points are avoided and only integer and fraction of integer is required.  
4. Arithmetic decoder: This is also a method in the class. The decoder do the rescaling at the exact moment and condition when the encoder encode the message. Besides, the algorithm is designed in the way that overflow will not happen. This is justified in the code where I use an example that the coded sequence is far larger than 20. Theoretically, it can be any length as what is required in real life.  
  
The encoder algorithm can only ensure that the range is larger than a quarter of the whole(2**precision). However, this is due to the inherent property of my implementation, instead of explicitly checking every time. I believe this is more efficient. Besides, it can reach near optimal result(near the entropy coded bits) even with only 4 bits precision.
