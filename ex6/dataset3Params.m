function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

Copt = [0.01;0.03;0.1;0.3;1;3;10;30];
sigmaopt = [0.01;0.03;0.1;0.3;1;3;10;30];

optionResults = zeros(64, 3);

resultIndex = 0;
for i=1:size(Copt)
  for j=1:size(sigmaopt)
    resultIndex = resultIndex + 1;
    
    model = svmTrain(X, y, Copt(i), @(x1, x2) gaussianKernel(x1, x2, sigmaopt(j)));
    predictions = svmPredict(model, Xval);
    
    optionResults(resultIndex, 1) = Copt(i);
    optionResults(resultIndex, 2) = sigmaopt(j);
    optionResults(resultIndex, 3) = mean(double(predictions ~= yval));
  endfor
endfor

[minError minIndex] = min(optionResults(:,3));

C = optionResults(minIndex, 1);
sigma = optionResults(minIndex, 2);

% =========================================================================

end
