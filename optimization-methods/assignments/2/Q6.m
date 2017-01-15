points = [
    0 0 0;
    4 0 0;
    0 2 0;
    0 0 2;
];

subplot(1,2,1);


count = 0;
for i=1:length(points)
    for j=i+1:length(points)
        for k=j+1:length(points)
            face = [points(i, :); points(j, :); points(k, :)];
            x = face(:, 1)';
            y = face(:, 2)';
            z = face(:, 3)';
            count = count + 1;
            fill3(x, y, z, count);
            hold on;
        end
    end
end
title('Q6-a');

xlabel('x1');
ylabel('x2');
zlabel('x3');

points = [
    0 0 0;
    4/3 4/3 0;
    0 2 0;
    0 0 2;
];
subplot(1, 2, 2);

count = 0;
for i=1:length(points)
    for j=i+1:length(points)
        for k=j+1:length(points)
            face = [points(i, :); points(j, :); points(k, :)];
            x = face(:, 1)';
            y = face(:, 2)';
            z = face(:, 3)';
            count = count + 1;
            fill3(x, y, z, count);
            hold on;
        end
    end
end
title('Q6-b');
xlabel('x1'); 
ylabel('x2'); 
zlabel('x3');