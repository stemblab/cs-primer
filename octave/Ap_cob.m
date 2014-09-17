resources

diaryinit('Ap.txt')
bl=ones(12,1); %. $b^\ell$
Ap=chipping_matrix(12); % $A^p$
diary on; disp((Ap*bl)'); diary off %. $A^p b^l$
