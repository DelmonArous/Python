clear all; clf; 
% Physical constants
m = 80;         % kg
rho = 1.293;    % kg/m^3
A = 0.45;       % m^2
C_D = 1.2;
w_med = 1;      % m/s
w_mot = -1;     % m/s
dt = 0.01;      % s
time = 10;      % s
t_c = 0.67;     % s
f_c = 488;      % N
f_v = 25.8;     % sN/m
% Initial conditions
v0 = 0;
x0 = 0;
% Numerical initialization
n = time/dt;
a_med = zeros(n, 1);
v_med = zeros(n, 1);
x_med = zeros(n, 1);
a_mot = zeros(n, 1);
v_mot = zeros(n, 1);
x_mot = zeros(n, 1);
t = zeros(n, 1);
F = zeros(n, 1);
F_C = zeros(n, 1);
F_V_medvind = zeros(n, 1);
F_V_motvind = zeros(n, 1);
D_medvind = zeros(n, 1);
D_motvind = zeros(n, 1);
% Set initial values
x_med(1) = x0;
x_mot(1) = x0;
v(1) = v0;
% Integration loop
for i = 1:n-1
    F(i) = 400;
    F_C(i) = f_c*exp(-(t(i)/t_c)^2);
    F_V_medvind(i) = f_v*v_med(i);
    F_V_motvind(i) = f_v*v_mot(i);
    D_medvind(i) = 0.5*A*(1-0.25*exp(-(t(i)/t_c)^2))*rho*C_D*(v_med(i)-w_med)^2;
    D_motvind(i) = 0.5*A*(1-0.25*exp(-(t(i)/t_c)^2))*rho*C_D*(v_mot(i)-w_mot)^2;
    
    F_net_med = F(i) + F_C(i) - F_V_medvind(i) - D_medvind(i);
    a_med(i+1) = F_net_med/m;
    v_med(i+1) = v_med(i) + a_med(i+1)*dt;
    x_med(i+1) = x_med(i) + v_med(i+1)*dt;
    
    F_net_mot = F(i) + F_C(i) - F_V_motvind(i) - D_motvind(i);
    a_mot(i+1) = F_net_mot/m;
    v_mot(i+1) = v_mot(i) + a_mot(i+1)*dt;
    x_mot(i+1) = x_mot(i) + v_mot(i+1)*dt;
    
    t(i+1) = t(i) + dt; 
end
disp(t)

% Plot results
subplot(2,1,1);
plot(t, x_med);
text(9.2, 99.9989,'\leftarrow 100m','HorizontalAlignment','left');
title('Plot of x(t); w = 1m/s')
xlabel('t [s]');
ylabel('x [m]');
subplot(2,1,2);
plot(t, x_mot);
text(9.42, 99.9470,'\leftarrow 100m','HorizontalAlignment','left');
title('Plot of x(t); w = -1m/s')
xlabel('t [s]');
ylabel('x [m]');