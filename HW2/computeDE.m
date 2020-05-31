
% eta: Decorrelation efficiency
% R1: Covariance matrix of the signal series after transformation
% R2: Covaraince amtrix of the original signal series 
function eta = computeDE(R1,R2)
    sum1 = 0.0;
    sum2 = 0.0;
    [L,~] = size(R1);
    for i = 1:L
       for j = 1:L
           if(i~=j)
               sum1 = sum1 + abs(R1(i,j));
               sum2 = sum2 + abs(R2(i,j));
           end
       end
    end
    eta = 1-(sum1/sum2);
end
