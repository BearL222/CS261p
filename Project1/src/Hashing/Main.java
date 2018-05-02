package Hashing;


import com.sun.tools.doclets.formats.html.SourceToHTMLConverter;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;

public class Main {
    static int capacity = 50000;
    static int testsNum = 48;
    static int sampleNum = 48000;
    static int testTimes = 300;

    public static void main(String[] args) {
        testing();
//        diffLoadFactor();
    }

    private static void diffLoadFactor() {
        // to store test information
        double[][][] results = new double[4][testsNum][3];

        Random rand = new Random();
        for(int i = 1; i <= 48; i++) {
            if(i % 10 == 0) System.out.println("10 finished");
            System.out.println("starting " + i);

            Hashing[] hashing = new Hashing[4];
            hashing[0] = new LinearHashing(capacity);
            hashing[1] = new ChainedHashing(capacity);
            hashing[2] = new CuckooHashing(capacity);
            hashing[3] = new QuadraticHashing(capacity);

            // generate test cases
            int[] tests = new int[i * capacity / 50];
            HashSet<Integer> set = new HashSet<>();
            for(int j = 0; j < tests.length; j++) {
                int tmp = rand.nextInt(capacity * 10);
                while(set.contains(tmp)) {
                    tmp = rand.nextInt(capacity * 10);
                }
                tests[i] = tmp;
                set.add(tmp);
                for(Hashing hash : hashing) {
                    hash.put(tmp, tmp);
                }
            }

            for(int k = 0; k < 10; k++) {
                // new random test cases
                int[] tests2 = new int[10000];
                for(int j = 0; j < tests2.length; j++) {
                    int tmp = rand.nextInt(capacity * 10);
                    while(set.contains(tmp)) {
                        tmp = rand.nextInt(capacity * 10);
                    }
                    tests2[j] = tmp;
                    set.add(tmp);
                }

                long startTime, endTime;
                for(int q = 0; q < 4; q++) {
                    for(int p = 0; p < 3; p++) {
                        startTime = System.currentTimeMillis();
                        Operation(hashing[q], p,tests2);
                        endTime = System.currentTimeMillis();
                        results[q][i - 1][p] += endTime - startTime;
                    }
                }
            }

            for(int q = 0; q < 4; q++) {
                for(int p = 0; p < 3; p++) {
                    results[q][i - 1][p] /= 10;
                }
            }
        }

        // print results
        for(double[][] result : results) {
            printResult(result);
        }
    }

    private static void Operation(Hashing hash, int type, int[] tests) {
        for(int test : tests) {
            if(type == 0) {
                hash.put(test, test);
            } else if(type == 1) {
                hash.get(test);
            } else {
                hash.remove(test);
            }
        }
    }

    private static void testing() {
        // to store test information
        long[][][] results = new long[4][testsNum][3];
        for(int k = 1; k <= testTimes; k++) {
            if(k % 20 == 0) {
                System.out.println("20 times finished");
            }

            // make random test cases
            int[] tests = new int[sampleNum];
            Random rand = new Random();
            HashSet<Integer> set = new HashSet<>();
            for(int i = 0; i < sampleNum; i++) {
                int test = rand.nextInt(capacity);
                while(set.contains(test)) {
                    test = rand.nextInt(capacity);
                }
                tests[i] = test;
            }

            for(int i = 1; i <= testsNum; i++) {
                Hashing[] hashing = new Hashing[4];
                hashing[0] = new LinearHashing(capacity);
                hashing[1] = new ChainedHashing(capacity);
                hashing[2] = new CuckooHashing(capacity);
                hashing[3] = new QuadraticHashing(capacity);

                for (int j = 0; j < 4; j++) {
                    sum(results[j][i - 1], calculate(hashing[j], Arrays.copyOfRange(tests, 0, i * capacity / 50)));
                }
            }
        }

        for(int i = 0; i < 4; i++) {
            printResult(mean(results[i], i));
        }
    }

    private static void testQua() {
        QuadraticHashing lh = new QuadraticHashing(11);
        lh.put(12,12);
        lh.put(26,26);
        lh.put(92,92);
        lh.put(23,23);
        lh.put(28,28);
        lh.put(94,94);
        lh.put(15,15);
        lh.remove(12);
        lh.remove(26);
        lh.remove(92);
        lh.remove(23);
        lh.remove(28);
        lh.remove(94);
        lh.remove(15);
        lh.get(12);
    }

    private static void sum(long[] a1, long[] a2) {
        for(int i = 0; i < a1.length; i++) {
            a1[i] += a2[i];
        }
    }

    private static double[][] mean(long[][] a, int type) {
        double[][] res = new double[a.length][3];
        for(int i = 0; i < a.length; i++) {
            int div = testTimes;
//            int div = testTimes * (i + 1) * 1000;
            for(int j = 0; j < 3; j++) {
                res[i][j] = (double)a[i][j] / div;
            }
        }
        return res;
    }

    private static void printResult(double[][] results) {
        DecimalFormat fmt = new DecimalFormat("#.###");
        for(int i = 0; i < 3; i++) {
            for (int j = 0; j < testsNum; j++) {
                System.out.print(fmt.format(results[j][i]) + ",");
            }
            System.out.println();
        }
    }

    private static long[] calculate(Hashing hashing, int[] tests) {
        long startTime, endTime;
        long[] results = new long[3];
        // put
        startTime = System.currentTimeMillis();
        for(int test : tests) {
            hashing.put(test, test);
        }
        endTime = System.currentTimeMillis();
        results[0] = endTime - startTime;
        // get
        startTime = System.currentTimeMillis();
        for(int test : tests) {
            hashing.get(test);
        }
        endTime = System.currentTimeMillis();
        results[1] = endTime - startTime;
        // remove
        startTime = System.currentTimeMillis();
        for(int test : tests) {
            hashing.remove(test);
        }
        endTime = System.currentTimeMillis();
        results[2] = endTime - startTime;
        return results;
    }
}
