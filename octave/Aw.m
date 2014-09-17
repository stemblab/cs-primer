resources

out1 = 'Aw-1.txt';
delete(out1);diary(out1);
disp(acc_dump_matrix(3,12,1)) % .$W_1$.
diary off

out2 = 'Aw-2.txt';
delete(out2);diary(out2);
Aw=[acc_dump_matrix(3,12,1); % $A_w$
    acc_dump_matrix(3,12,2);
    acc_dump_matrix(3,12,3);
    acc_dump_matrix(3,12,4)]
diary off

