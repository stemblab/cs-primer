resources

% $Ax=b$ dimensions...
N = 128;  % columns in $A$
M = 32;   % rows in $A$
K = 5;    % nonzero elements of $x$ %.
%%%%%

x = zeros(N,1); % .initialize $x$.
x(randperm(N,K)) = 1*exp(j*2*pi*rand(1,K)); % .$K$ values. have random phase

Al = inv(dftmtx(N)); % .COB/iDFT. $A^\ell$
bl = Al*x; % .Nyquist samples. $b^\ell$

samp_idx = randperm(N,M); % .randomly select $M$ rows.
b = bl(samp_idx); % discard rows: $b^\ell \rightarrow b$
A = Al(samp_idx,:); % discard rows: .$A^\ell \rightarrow A$.

hold on

plot(real(bl), '.b-')

green = [0.5, 0.75, 0.5];
plot(imag(bl),'.-', 'color', green);

plot(samp_idx,real(b),'bo', 'markersize', 4);
plot(samp_idx, imag(b), 'o', 
    'markersize', 4,
    'color', green, 
    'markeredgecolor', green);

xlabel('sample')
ylabel('value')
ax=axis; axis([1 N ax(3:4)])
legend('real (Nyq)','imag (Nyq)','real (comp)','imag (comp)',-1)

print -dsvg nus_nyq_samp.svg

x2=irls(A,b); % .solve $Ax=b$ with IRLS.

clf;hold on
plot(x,'bo')
plot(x2,'rx')
xlabel('real(x)')
ylabel('imag(x)')
l=legend('original','recovered',-1);
plot(exp(j*linspace(0,2*pi,32)),'.','markersize',3)
axis(1.1*[-1 1 -1 1])
grid on

print -dsvg nus.svg


