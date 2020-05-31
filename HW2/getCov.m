 
% generate a 8*8 adjacent covariance matrix
function cov = getCov(rho)
    cov = zeros(8,8);
    for i = 1:8
        for j = 1:8
            cov(i,j) = rho^(abs(i-j));
        end
    end
end

