%% Path
clear;
% relative paths can terminates early; so use absolute
path_home = '/Users/chovey/Brief/book/fig';
addpath(path_home);

pdf_output = 1; % 0 for no pdf output, 1 for pdf output

%% Utilities
LightGray = [0.9 0.9 0.9];
MediumGray = [0.5 0.5 0.5];
DarkGray = [0.1 0.1 0.1];
DarkGreen = [0.0 0.4 0.0];
DeepCadmiumRed = [0.88 0.09 0.05];
LightBlue = [50 100 256]/256;

%% Plot
x = 0:0.01:3;
y_lag = 0.5*(x.^2 - 1);
y_eng = x - 1;
y_log = log(x);
y_true = 1 - (1./x);
y_eul = 0.5*(1 - (1./x).^2);
h=figure(1);
clf;

e2 = plot(x,y_lag,'Color','b','LineWidth',3);
hold on;
e1 = plot(x,y_eng,'Color','k','LineWidth',0.5);
e0 = plot(x,y_log,'Color',DeepCadmiumRed,'LineStyle',':','LineWidth',3);
en1 = plot(x,y_true,'Color',DarkGreen,'LineStyle','-.','LineWidth',2);
en2 = plot(x,y_eul,'Color',MediumGray,'LineWidth',2','LineStyle','--');

grid on;
grid minor;
ax = gca;
ax.GridColor = DarkGray;
ax.GridAlpha = 0.5;
ax.GridLineStyle = '-';
axis equal;
axis([0 3 -2 2]);
xticks(0:1:3);
%xticklabels({'0','','1','','2','','3'});
yticks(-2:1:2);
%yticklabels({'-2','','-1','','0','','1','','2'});
xlabel('$\mbox{stretch} \; \lambda = \frac{\ell}{L_0}$','interpreter','latex');
ylabel('$\mbox{strain} \; f(\lambda)$','interpreter','latex');
legend({'Lagrange', 'Engineering (Biot)', ...
    'Log (Hencky, Natural)', 'True', ...
    'Eulieran'}, ...
    'Location','SouthEast','interpreter','latex');


%% Output
if pdf_output
    pdf_string = 'strain_v_stretch';
    cd(path_home);
    fig = gcf;
    set(fig, 'PaperOrientation','portrait');
    set(fig, 'PaperUnits','normalized');
    set(fig, 'PaperPosition', [0 0 1 1]);
    saveas(fig, pdf_string, 'pdf');
end