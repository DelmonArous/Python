time = 10.0;
dt = 0.001;
m = 23;
U0 = 150.0;
x0 = 2.0;
alpha = 39.48;

n = ceil(time/dt);

x = zeros(n,1);
v = zeros(n,1);
t = zeros(n,1);

x(1) = -5.0;
v(1) = 8.0;

for i = 1:n-1
    
    if ((-x0 < x(i)) && (x(i) < 0))
        F = (U0/x0) - alpha*v(i);
    elseif ((0 < x(i)) && (x(i) < x0))
        F = -(U0/x0) - alpha*v(i);
    else
        F = 0;
    end
        
    a = F/m;
    v(i+1) = v(i) + dt*a;
    x(i+1) = x(i) + dt*v(i+1);
    t(i+1) = t(i) + dt;
end

plot(t,x)
xlabel('t')
ylabel('x')
title(['Plot of the movement for the particle with v_0 =' num2str(v(1))])
