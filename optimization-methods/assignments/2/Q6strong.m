points = [   
    4 0 0;
    0 2 0;
    0 0 2;
]
X = points(:,1);
Y = points(:,2);
Z = points(:,3);
subplot(1, 2, 1);
fill3(X, Y, Z, 1);
xlabel('x_1'), ylabel('x_2'), zlabel('x_3');
title('Q6-a');

points = [
    0 0 2;
    4/3 4/3 0;
];

X = points(:,1);
Y = points(:,2);
Z = points(:,3);
subplot(1, 2, 2);
plot3(X, Y, Z);
xlabel('x_1'), ylabel('x_2'), zlabel('x_3');
title('Q6-b');
