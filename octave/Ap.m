resources
bl=ones(12,1); % $b^\ell$
Ap=chipping_matrix(12); % $A^p$

out1 = 'Ap.txt';
delete(out1);diary(out1);
disp(['[' num2str((Ap*bl)') ']^T']); % $A^p b^\ell$
diary off
