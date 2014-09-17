resources

K=5; % number of tones in $s(t)$
M=32; % compressed sampling rate
N=128; % Nyquist sampling rate

% We use an initial DST, rather than DFT, to keep the computation real
% for $\ell_1$-magic below.

Al=sin((pi/N)*[1:N]'*[1:N]); % COB matrix: $A^\ell$

% Code for the "chipping" matrix $A^p$ and the "Walsh" matrix $A^w$ is
% imported from <a href="?id=b007g#functions">Reproducing "Beyond Nyquist..."</a>

Ap=chipping_matrix(N);

Aw=[acc_dump_matrix(M,N,1);
    acc_dump_matrix(M,N,2);
    acc_dump_matrix(M,N,3);
    acc_dump_matrix(M,N,4)];
    
% The composite change of basis is $A^w A^p A^\ell$

As=Aw*Ap*Al;

% The COB matrix, $A$ (of $Ax=b$) is the first $M$ rows

A=As(1:M,:);

% We pick a random $x$

x=zeros(N,1); % $x$ as mostly zeros
x(randperm(N,K))=1; % except for $K$ ones

% samples

b=A*x;                      % compressed ($b$)
bs=As*x;                    % Nyquist ($b^\ell$)

%!end (116)

subplot(2,1,1);hold on
plot(Al*x,'.b-');
c = [0.5, 0.75, 0.5];
plot(Ap*Al*x, 'o-', 
    'markersize', 4, 
    'color', c, 
    'markeredgecolor', c);
ax=axis; axis([0 N ax(3:4)]);
l=legend('bl','Ap*bl',-1);
ylabel('value')
xlabel('sample')
subplot(2,1,2); hold on
plot(Aw*Ap*Al*x,'.r-')
plot(A*x,'om-', 'markersize', 4)
ylabel('value')
xlabel('sample')
ax=axis; axis([0 N ax(3:4)]);
l=legend('Aw*Ap*bl', 'b',-1);

print -dsvg rand_demod.svg

x_rec=l1eq_pd(zeros(128,1),A,[],b,1e-4); % recovered $x$

close all
hold on
plot(x,'.b');
h = stem(x_rec,'r');
set(h, 'markersize', 4);
axis('square');
xlabel('frequency (Hz)');
ylabel('tone amplitude');
l=legend('input x','recovered x',-1);
axis([1 128 -0.2 1.2]);

print -dsvg rand_demod_recon.svg


