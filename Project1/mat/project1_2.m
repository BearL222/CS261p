data = [100,203,308,415,524,635,747,861,977,1095,1215,1336,1460,1585,1713,1842,1973,2107,2243,2380,2521,2662,2806,2952,3103,3255,3411,3569,3731,3896,4064,4236,4410,4590,4777,4967,5159,5361,5569,5781,6006,6295,7243,7854,7769,8804,10381,12339,16189,26883,40808,82157,
100,203,308,415,524,635,747,860,976,1093,1212,1332,1454,1578,1703,1830,1957,2087,2218,2351,2485,2619,2755,2892,3031,3170,3312,3455,3598,3743,3889,4035,4183,4332,4482,4633,4785,4938,5091,5246,5402,5558,5713,5871,6030,6187,6345,6501,6658,6800,6949,7010,
200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200,5400,5600,5800,6000,6200,6400,6600,6800,7000,7200,7400,7600,7800,8000,8200,8400,8600,8800,9000,9200,9400,9600,9800,10000,10200,10400];

[m,n] = size(data);
testNum = zeros(1,n);
for i = 1:n
    testNum(i) = i * 100;
end

figure,
for i = 1:3
%     subplot(1,3,i)
    figure,
    plot(testNum, data(i,:));
    xlabel("Number of test cases");
    ylabel("Number of collisions");
end
