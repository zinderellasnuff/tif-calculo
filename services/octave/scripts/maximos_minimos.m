% =========================================================================
% TIF Cálculo Fase III - UCSM 2025
% Autor: Aron
% Script: Máximos y Mínimos con GNU Octave
% =========================================================================

fprintf('\n');
fprintf('========================================================================\n');
fprintf('  ANÁLISIS DE MÁXIMOS Y MÍNIMOS CON GNU OCTAVE\n');
fprintf('  TIF Cálculo Fase III - UCSM 2025\n');
fprintf('========================================================================\n\n');

% Cargar paquete simbólico
pkg load symbolic

% =========================================================================
% EJEMPLO 1: f(x) = 3x² - 12x + 5 en [0, 3]
% =========================================================================

fprintf('EJEMPLO 1: f(x) = 3x² - 12x + 5 en [0, 3]\n');
fprintf('------------------------------------------------------------------------\n');

% Definir variable simbólica
syms x

% Definir función
f1 = 3*x^2 - 12*x + 5;
fprintf('Función: f(x) = ');
disp(f1);

% Primera derivada
f1_prime = diff(f1, x);
fprintf('\nPrimera derivada: f''(x) = ');
disp(f1_prime);

% Encontrar puntos críticos
critical_points1 = solve(f1_prime == 0, x);
fprintf('Puntos críticos: ');
disp(double(critical_points1));

% Intervalo
a1 = 0;
b1 = 3;

% Evaluar en puntos críticos y extremos del intervalo
fprintf('\nEvaluación en puntos:\n');
points_to_eval1 = [a1; double(critical_points1); b1];

for i = 1:length(points_to_eval1)
    pt = points_to_eval1(i);
    val = double(subs(f1, x, pt));
    fprintf('  f(%.2f) = %.4f\n', pt, val);
end

% Determinar máximo y mínimo absoluto
values1 = arrayfun(@(pt) double(subs(f1, x, pt)), points_to_eval1);
[max_val1, max_idx1] = max(values1);
[min_val1, min_idx1] = min(values1);

fprintf('\nConclusión:\n');
fprintf('  ✓ Máximo absoluto: f(%.2f) = %.4f\n', points_to_eval1(max_idx1), max_val1);
fprintf('  ✓ Mínimo absoluto: f(%.2f) = %.4f\n', points_to_eval1(min_idx1), min_val1);

% Graficar (solo si está disponible)
try
    figure(1);
    x_vals1 = linspace(a1-0.5, b1+0.5, 500);
    y_vals1 = double(subs(f1, x, x_vals1));
    plot(x_vals1, y_vals1, 'b-', 'LineWidth', 2);
    hold on;

    % Marcar puntos
    plot(points_to_eval1(max_idx1), max_val1, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
    plot(points_to_eval1(min_idx1), min_val1, 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'g');

    % Líneas de intervalo
    line([a1 a1], ylim, 'Color', 'k', 'LineStyle', '--');
    line([b1 b1], ylim, 'Color', 'k', 'LineStyle', '--');

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('Ejemplo 1: f(x) = 3x² - 12x + 5 en [0, 3]');
    legend('f(x)', 'Máximo absoluto', 'Mínimo absoluto', 'Location', 'best');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 1)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n\n');

% =========================================================================
% EJEMPLO 2: f(x) = 2x³ - 3x² - 12x + 1 en [-2, 3]
% =========================================================================

fprintf('EJEMPLO 2: f(x) = 2x³ - 3x² - 12x + 1 en [-2, 3]\n');
fprintf('------------------------------------------------------------------------\n');

% Definir función
f2 = 2*x^3 - 3*x^2 - 12*x + 1;
fprintf('Función: f(x) = ');
disp(f2);

% Primera derivada
f2_prime = diff(f2, x);
fprintf('\nPrimera derivada: f''(x) = ');
disp(f2_prime);

% Segunda derivada
f2_double_prime = diff(f2_prime, x);
fprintf('Segunda derivada: f''''(x) = ');
disp(f2_double_prime);

% Encontrar puntos críticos
critical_points2 = solve(f2_prime == 0, x);
fprintf('\nPuntos críticos: ');
disp(double(critical_points2));

% Intervalo
a2 = -2;
b2 = 3;

% Evaluar en puntos críticos y extremos
fprintf('\nEvaluación:\n');
points_to_eval2 = [a2; double(critical_points2); b2];

for i = 1:length(points_to_eval2)
    pt = points_to_eval2(i);
    val = double(subs(f2, x, pt));
    fprintf('  f(%.2f) = %.4f\n', pt, val);
end

% Clasificar puntos críticos usando segunda derivada
fprintf('\nClasificación de puntos críticos:\n');
for i = 1:length(critical_points2)
    pt = double(critical_points2(i));
    f_double = double(subs(f2_double_prime, x, pt));

    fprintf('  x = %.4f:\n', pt);
    fprintf('    f''''(%.4f) = %.4f\n', pt, f_double);

    if f_double > 0
        fprintf('    → MÍNIMO LOCAL (f'''' > 0)\n');
    elseif f_double < 0
        fprintf('    → MÁXIMO LOCAL (f'''' < 0)\n');
    else
        fprintf('    → Criterio no concluyente (f'''' = 0)\n');
    end
end

% Determinar extremos absolutos
values2 = arrayfun(@(pt) double(subs(f2, x, pt)), points_to_eval2);
[max_val2, max_idx2] = max(values2);
[min_val2, min_idx2] = min(values2);

fprintf('\nExtremos absolutos en [%.0f, %.0f]:\n', a2, b2);
fprintf('  ✓ Máximo absoluto: f(%.2f) = %.4f\n', points_to_eval2(max_idx2), max_val2);
fprintf('  ✓ Mínimo absoluto: f(%.2f) = %.4f\n', points_to_eval2(min_idx2), min_val2);

% Graficar
try
    figure(2);
    x_vals2 = linspace(a2-0.5, b2+0.5, 500);
    y_vals2 = double(subs(f2, x, x_vals2));
    plot(x_vals2, y_vals2, 'b-', 'LineWidth', 2);
    hold on;

    % Marcar extremos absolutos
    plot(points_to_eval2(max_idx2), max_val2, 'ro', 'MarkerSize', 12, 'MarkerFaceColor', 'r');
    plot(points_to_eval2(min_idx2), min_val2, 'go', 'MarkerSize', 12, 'MarkerFaceColor', 'g');

    % Marcar otros puntos críticos
    for i = 1:length(critical_points2)
        pt = double(critical_points2(i));
        if pt ~= points_to_eval2(max_idx2) && pt ~= points_to_eval2(min_idx2)
            val = double(subs(f2, x, pt));
            plot(pt, val, 'yo', 'MarkerSize', 10, 'MarkerFaceColor', 'y');
        end
    end

    % Líneas de intervalo
    line([a2 a2], ylim, 'Color', 'k', 'LineStyle', '--');
    line([b2 b2], ylim, 'Color', 'k', 'LineStyle', '--');

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('Ejemplo 2: f(x) = 2x³ - 3x² - 12x + 1 en [-2, 3]');
    legend('f(x)', 'Máximo absoluto', 'Mínimo absoluto', 'Punto crítico', 'Location', 'best');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 2)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n');

% =========================================================================
% EJEMPLO 3: f(x) = x + 4/x en [0.5, 4]
% =========================================================================

fprintf('\nEJEMPLO 3: f(x) = x + 4/x en [0.5, 4]\n');
fprintf('------------------------------------------------------------------------\n');

% Definir función
f3 = x + 4/x;
fprintf('Función: f(x) = ');
disp(f3);

% Primera derivada
f3_prime = diff(f3, x);
fprintf('\nPrimera derivada: f''(x) = ');
disp(f3_prime);
fprintf('Simplificada: ');
disp(simplify(f3_prime));

% Puntos críticos
critical_points3 = solve(f3_prime == 0, x);
% Filtrar solo valores reales positivos
critical_points3_real = [];
for i = 1:length(critical_points3)
    pt = double(critical_points3(i));
    if isreal(pt) && pt > 0
        critical_points3_real = [critical_points3_real; pt];
    end
end

fprintf('\nPuntos críticos (reales positivos): ');
disp(critical_points3_real);

% Intervalo
a3 = 0.5;
b3 = 4;

% Filtrar puntos en el intervalo
critical_in_interval = critical_points3_real(critical_points3_real >= a3 & critical_points3_real <= b3);

% Evaluar
fprintf('\nEvaluación:\n');
points_to_eval3 = [a3; critical_in_interval; b3];

for i = 1:length(points_to_eval3)
    pt = points_to_eval3(i);
    val = double(subs(f3, x, pt));
    fprintf('  f(%.4f) = %.4f\n', pt, val);
end

% Extremos absolutos
values3 = arrayfun(@(pt) double(subs(f3, x, pt)), points_to_eval3);
[max_val3, max_idx3] = max(values3);
[min_val3, min_idx3] = min(values3);

fprintf('\nConclusión:\n');
fprintf('  ✓ Máximo absoluto: f(%.4f) = %.4f\n', points_to_eval3(max_idx3), max_val3);
fprintf('  ✓ Mínimo absoluto: f(%.4f) = %.4f\n', points_to_eval3(min_idx3), min_val3);

% Graficar
try
    figure(3);
    x_vals3 = linspace(a3, b3, 500);
    y_vals3 = double(subs(f3, x, x_vals3));
    plot(x_vals3, y_vals3, 'b-', 'LineWidth', 2);
    hold on;

    plot(points_to_eval3(max_idx3), max_val3, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
    plot(points_to_eval3(min_idx3), min_val3, 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'g');

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('Ejemplo 3: f(x) = x + 4/x en [0.5, 4]');
    legend('f(x)', 'Máximo absoluto', 'Mínimo absoluto', 'Location', 'best');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 3)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n');
fprintf('========================================================================\n');
fprintf('  FIN DEL ANÁLISIS\n');
fprintf('========================================================================\n');
fprintf('\n');

% Descarga del paquete
pkg unload symbolic
