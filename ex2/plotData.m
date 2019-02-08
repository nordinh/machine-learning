function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%
positiveResults = find(y==1);
negativeResults = find(y==0);

plot(X(positiveResults,1), X(positiveResults,2), 'k+', 'linewidth', 2);
plot(X(negativeResults,1), X(negativeResults,2), 'ko', 'markerfacecolor', 'y');




% =========================================================================



hold off;

end
