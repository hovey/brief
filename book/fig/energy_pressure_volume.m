clc; clear; % clear screen, clear all variables

%% Ouput
pdf_output = 1; % 0 for no print, 1 for print

% kg/m^3 = 10 g/cc, e.g., copper density is 8,940 kg/m^3
V0 = 1/10^3; % m^3/kg
V1 = 1/10^5; % m^3/kg
n_intervals = 10;
V_magnitude = V0 - V1; % m^3/kg
delta_V = V_magnitude / n_intervals; % m^3/kg
V = V1:delta_V:V0; % k/m^3

P0 = 0; % N/m^2 
P1 = 10^5; % N/m^2
P_magnitude = P1 - P0; % N/m^2
delta_P = P_magnitude / n_intervals; % N/m^2
P = P0:delta_P:P1; % N/m^2

figure(1);
clf;
hold on;
for i=1:n_intervals
   plot(P,-0.5*(P + P0)*(V(i) - V0));
   a=4;
end
xlabel('Pressure (N/m^2)');
ylabel('Energy Change (Nm)');

figure(2);
clf;
hold on;
for i=1:n_intervals
   plot(V,-0.5*(P(i) + P0)*(V - V0)); 
   a=4;
end
xlabel('Specific Volume (m^3/kg)');
ylabel('Energy Change (Nm)');


figure(3);
clf;
hold on;
surfc(V,P,-0.5*(P + P0).*(V - V0));

return;


E1_E0 = -0.5*(P - P0).*(V - V0)

