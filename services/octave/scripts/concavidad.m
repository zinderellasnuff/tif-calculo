% =========================================================================
% TIF Cálculo Fase III - UCSM 2025
% Autor: Aron
% Script: Análisis de Concavidad con GNU Octave
% =========================================================================

fprintf('\n');
fprintf('========================================================================\n');
fprintf('  ANÁLISIS DE CONCAVIDAD Y PUNTOS DE INFLEXIÓN\n');
fprintf('  TIF Cálculo Fase III - UCSM 2025\n');
fprintf('========================================================================\n\n');

% Cargar paquete simbólico
pkg load symbolic

% =========================================================================
% EJEMPLO 1: f(x) = x³ - 3x²
% =========================================================================

fprintf('EJEMPLO 1: Análisis de Concavidad - f(x) = x³ - 3x²\n');
fprintf('------------------------------------------------------------------------\n');

% Definir variable y función
syms x
f1 = x^3 - 3*x^2;
fprintf('Función: f(x) = ');
disp(f1);

% Primera derivada
f1_prime = diff(f1, x);
fprintf('\nPrimera derivada: f''(x) = ');
disp(f1_prime);

% Segunda derivada
f1_double_prime = diff(f1_prime, x);
fprintf('Segunda derivada: f''''(x) = ');
disp(f1_double_prime);

% Candidatos a puntos de inflexión (f'' = 0)
inflection_candidates1 = solve(f1_double_prime == 0, x);
fprintf('\nCandidatos a inflexión (f'''' = 0): ');
disp(double(inflection_candidates1));

% Análisis de concavidad
fprintf('\nANÁLISIS DE CONCAVIDAD:\n');
fprintf('------------------------------------------------------------------------\n');

for i = 1:length(inflection_candidates1)
    if isreal(double(inflection_candidates1(i)))
        c = double(inflection_candidates1(i));
        fprintf('\nEn x = %.4f:\n', c);

        % Evaluar f'' antes y después
        before = double(subs(f1_double_prime, x, c - 0.1));
        after = double(subs(f1_double_prime, x, c + 0.1));

        fprintf('  f''''(%.1f) = %.4f\n', c - 0.1, before);
        fprintf('  f''''(%.1f) = %.4f\n', c + 0.1, after);

        % Verificar cambio de signo
        if before * after < 0
            y_val = double(subs(f1, x, c));
            fprintf('  ✓ HAY punto de inflexión en (%.4f, %.4f)\n', c, y_val);

            if before < 0
                fprintf('    Cambia de cóncava abajo a cóncava arriba\n');
            else
                fprintf('    Cambia de cóncava arriba a cóncava abajo\n');
            end
        else
            fprintf('  ✗ NO hay cambio de concavidad\n');
        end
    end
end

% Graficar
try
    figure(1);
    x_vals1 = linspace(-2, 5, 500);
    y_vals1 = double(subs(f1, x, x_vals1));
    y_double_prime1 = double(subs(f1_double_prime, x, x_vals1));

    subplot(2, 1, 1);
    plot(x_vals1, y_vals1, 'b-', 'LineWidth', 2);
    hold on;

    % Marcar punto de inflexión
    for i = 1:length(inflection_candidates1)
        c = double(inflection_candidates1(i));
        y_c = double(subs(f1, x, c));
        plot(c, y_c, 'rd', 'MarkerSize', 12, 'MarkerFaceColor', 'r');
    end

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('f(x) = x³ - 3x²');
    legend('f(x)', 'Punto de inflexión', 'Location', 'best');
    hold off;

    subplot(2, 1, 2);
    plot(x_vals1, y_double_prime1, 'p-', 'LineWidth', 2, 'Color', [0.5, 0, 0.5]);
    hold on;
    line(xlim, [0 0], 'Color', 'k', 'LineStyle', '--');
    grid on;
    xlabel('x');
    ylabel('f''''(x)');
    title('Segunda Derivada - Criterio de Concavidad');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 1)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n\n');

% =========================================================================
% EJEMPLO 2: f(x) = 3x⁴ - 4x³ - 12x² + 5
% =========================================================================

fprintf('EJEMPLO 2: Múltiples Puntos de Inflexión - f(x) = 3x⁴ - 4x³ - 12x² + 5\n');
fprintf('------------------------------------------------------------------------\n');

% Definir función
f2 = 3*x^4 - 4*x^3 - 12*x^2 + 5;
fprintf('Función: f(x) = ');
disp(f2);

% Derivadas
f2_prime = diff(f2, x);
f2_double_prime = diff(f2_prime, x);

fprintf('\nPrimera derivada: f''(x) = ');
disp(f2_prime);

fprintf('Segunda derivada: f''''(x) = ');
disp(f2_double_prime);
fprintf('Factorizada: ');
disp(factor(f2_double_prime));

% Puntos críticos
critical_points2 = solve(f2_prime == 0, x);
fprintf('\nPuntos críticos (f'' = 0): ');
disp(double(critical_points2));

% Puntos de inflexión
inflection_candidates2 = solve(f2_double_prime == 0, x);
fprintf('Candidatos a inflexión (f'''' = 0): ');
disp(double(inflection_candidates2));

% Tabla de análisis
fprintf('\n');
fprintf('========================================================================\n');
fprintf('TABLA DE ANÁLISIS COMPLETO\n');
fprintf('========================================================================\n');
fprintf('%-20s %-15s %-25s\n', 'Intervalo', 'f''''(x)', 'Concavidad');
fprintf('------------------------------------------------------------------------\n');

% Ordenar puntos de inflexión
inflection_pts2 = sort(double(inflection_candidates2));

% Puntos de prueba
test_points = [inflection_pts2(1) - 1, ...
               (inflection_pts2(1) + inflection_pts2(2))/2, ...
               inflection_pts2(2) + 1];

intervals = {sprintf('(-∞, %.2f)', inflection_pts2(1)), ...
             sprintf('(%.2f, %.2f)', inflection_pts2(1), inflection_pts2(2)), ...
             sprintf('(%.2f, ∞)', inflection_pts2(2))};

for i = 1:length(test_points)
    f_double = double(subs(f2_double_prime, x, test_points(i)));
    if f_double > 0
        concavity = 'Cóncava arriba ⌣';
        sign = sprintf('+ (%.2f)', f_double);
    else
        concavity = 'Cóncava abajo ⌢';
        sign = sprintf('- (%.2f)', f_double);
    end
    fprintf('%-20s %-15s %-25s\n', intervals{i}, sign, concavity);
end

fprintf('------------------------------------------------------------------------\n');

% Puntos de inflexión confirmados
fprintf('\nPuntos de inflexión:\n');
for i = 1:length(inflection_pts2)
    y_ip = double(subs(f2, x, inflection_pts2(i)));
    fprintf('  ✓ (%.4f, %.4f)\n', inflection_pts2(i), y_ip);
end

% Graficar
try
    figure(2);
    x_vals2 = linspace(-2, 3, 500);
    y_vals2 = double(subs(f2, x, x_vals2));
    y_double_prime2 = double(subs(f2_double_prime, x, x_vals2));

    % Separar por concavidad
    concave_up_idx = y_double_prime2 > 0;
    concave_down_idx = y_double_prime2 < 0;

    plot(x_vals2(concave_up_idx), y_vals2(concave_up_idx), 'g-', 'LineWidth', 3);
    hold on;
    plot(x_vals2(concave_down_idx), y_vals2(concave_down_idx), 'r-', 'LineWidth', 3);

    % Puntos de inflexión
    for i = 1:length(inflection_pts2)
        y_ip = double(subs(f2, x, inflection_pts2(i)));
        plot(inflection_pts2(i), y_ip, 'md', 'MarkerSize', 15, 'MarkerFaceColor', 'm');
    end

    % Puntos críticos
    for i = 1:length(critical_points2)
        if isreal(double(critical_points2(i)))
            cp = double(critical_points2(i));
            y_cp = double(subs(f2, x, cp));
            plot(cp, y_cp, 'yo', 'MarkerSize', 10, 'MarkerFaceColor', 'y');
        end
    end

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('Análisis de Concavidad: f(x) = 3x⁴ - 4x³ - 12x² + 5');
    legend('Cóncava arriba', 'Cóncava abajo', 'Inflexión', 'Crítico', 'Location', 'best');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 2)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n\n');

% =========================================================================
% EJEMPLO 3: Análisis Combinado - f(x) = x³ - 3x² - 9x + 4
% =========================================================================

fprintf('EJEMPLO 3: Análisis Combinado - f(x) = x³ - 3x² - 9x + 4\n');
fprintf('------------------------------------------------------------------------\n');

% Definir función
f3 = x^3 - 3*x^2 - 9*x + 4;
fprintf('Función: f(x) = ');
disp(f3);

% Derivadas
f3_prime = diff(f3, x);
f3_double_prime = diff(f3_prime, x);

fprintf('\nf''(x) = ');
disp(f3_prime);
fprintf('f''''(x) = ');
disp(f3_double_prime);

% Puntos críticos
critical_points3 = solve(f3_prime == 0, x);
fprintf('\nPuntos críticos: ');
disp(double(critical_points3));

% Puntos de inflexión
inflection_points3 = solve(f3_double_prime == 0, x);
fprintf('Puntos de inflexión: ');
disp(double(inflection_points3));

% Clasificar puntos críticos
fprintf('\nCLASIFICACIÓN DE EXTREMOS (usando criterio de segunda derivada):\n');
fprintf('------------------------------------------------------------------------\n');

for i = 1:length(critical_points3)
    if isreal(double(critical_points3(i)))
        cp = double(critical_points3(i));
        f_val = double(subs(f3, x, cp));
        f_double = double(subs(f3_double_prime, x, cp));

        fprintf('\nx = %.4f:\n', cp);
        fprintf('  f(%.4f) = %.4f\n', cp, f_val);
        fprintf('  f''''(%.4f) = %.4f\n', cp, f_double);

        if f_double > 0
            fprintf('  ✓ MÍNIMO LOCAL (f'''' > 0, cóncava arriba)\n');
        elseif f_double < 0
            fprintf('  ✓ MÁXIMO LOCAL (f'''' < 0, cóncava abajo)\n');
        else
            fprintf('  ⚠ Criterio no concluyente (f'''' = 0)\n');
        end
    end
end

fprintf('\nPUNTOS DE INFLEXIÓN:\n');
fprintf('------------------------------------------------------------------------\n');
for i = 1:length(inflection_points3)
    if isreal(double(inflection_points3(i)))
        ip = double(inflection_points3(i));
        f_val = double(subs(f3, x, ip));
        fprintf('  ✓ Inflexión en (%.4f, %.4f)\n', ip, f_val);
        fprintf('    La concavidad cambia de sentido\n');
    end
end

% Graficar
try
    figure(3);
    x_vals3 = linspace(-3, 5, 500);
    y_vals3 = double(subs(f3, x, x_vals3));

    plot(x_vals3, y_vals3, 'b-', 'LineWidth', 3);
    hold on;

    % Puntos críticos
    for i = 1:length(critical_points3)
        if isreal(double(critical_points3(i)))
            cp = double(critical_points3(i));
            f_val = double(subs(f3, x, cp));
            f_double = double(subs(f3_double_prime, x, cp));

            if f_double > 0
                plot(cp, f_val, 'go', 'MarkerSize', 15, 'MarkerFaceColor', 'g');
            else
                plot(cp, f_val, 'ro', 'MarkerSize', 15, 'MarkerFaceColor', 'r');
            end
        end
    end

    % Puntos de inflexión
    for i = 1:length(inflection_points3)
        if isreal(double(inflection_points3(i)))
            ip = double(inflection_points3(i));
            f_val = double(subs(f3, x, ip));
            plot(ip, f_val, 'md', 'MarkerSize', 15, 'MarkerFaceColor', 'm');
        end
    end

    grid on;
    xlabel('x');
    ylabel('f(x)');
    title('Análisis Completo: f(x) = x³ - 3x² - 9x + 4');
    legend('f(x)', 'Mínimo local', 'Máximo local', 'Punto de inflexión', 'Location', 'best');
    hold off;

    fprintf('\n✓ Gráfica generada (Figura 3)\n');
catch
    fprintf('\nNota: Gráfica no disponible en modo sin interfaz gráfica\n');
end

fprintf('\n');
fprintf('========================================================================\n');
fprintf('  RESUMEN DE CRITERIOS\n');
fprintf('========================================================================\n');
fprintf('\n');
fprintf('CRITERIO DE CONCAVIDAD:\n');
fprintf('  • f''''(x) > 0 → Función cóncava hacia ARRIBA ⌣\n');
fprintf('  • f''''(x) < 0 → Función cóncava hacia ABAJO ⌢\n');
fprintf('\n');
fprintf('PUNTOS DE INFLEXIÓN:\n');
fprintf('  • Candidatos donde f''''(x) = 0 o f'''' no existe\n');
fprintf('  • Verificar cambio de signo de f''''\n');
fprintf('\n');
fprintf('RELACIÓN CON EXTREMOS:\n');
fprintf('  • En un MÍNIMO local: f''''(x) > 0 (cóncava arriba)\n');
fprintf('  • En un MÁXIMO local: f''''(x) < 0 (cóncava abajo)\n');
fprintf('\n');
fprintf('========================================================================\n');
fprintf('  FIN DEL ANÁLISIS\n');
fprintf('========================================================================\n');
fprintf('\n');

% Descargar paquete
pkg unload symbolic
