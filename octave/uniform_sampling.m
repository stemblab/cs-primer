resources

% $$\def\spark#1{\mathrm{spark} \begin{bmatrix}#1\end{bmatrix}}$$
Al=[1 -1 1;1 0 0;1 1 1];         % $A^\ell$

out = 'uniform_sampling-1.txt';
delete(out);diary(out);
spark_del_1=spark(Al([2 3],:))   % $\spark{1&0&0\\1&1&1}$
spark_del_2=spark(Al([1 3],:))   % $\spark{1&-1&1\\1&1&1}$
spark_del_3=spark(Al([1 2],:))   % $\spark{1&-1&1\\1&0&0}$
diary off

th=pi/4; % $\theta$

% <a href="http://wikipedia.org/wiki/Rotation_matrix">Rotation matrix</a>.
R=[cos(th) -sin(th) 0; sin(th) cos(th) 0; 0 0 1]; 

An=R*Al; % $A^n = R A^\ell $

out = 'uniform_sampling-2.txt';
delete(out);diary(out);
spark_del_1=spark(An([2 3],:))
spark_del_2=spark(An([1 3],:))
spark_del_3=spark(An([1 2],:))
diary off

out = 'uniform_sampling-3.txt';
delete(out);diary(out);
disp(R)
diary off
