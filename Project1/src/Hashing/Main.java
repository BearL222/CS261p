package Hashing;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;

public class Main {
    static int capacity = 5000;
    static int testsNum = 48;
    static int sampleNum = 4800;
    static int testTimes = 40;
    static int loopTimes4LoadFactor = 20;

    public static void main(String[] args) {
        sequenceTest();
//        diffLoadFactor();
    }

    private static void diffLoadFactor() {
        // to store test information
        long[][][] results = new long[4][testsNum][3];
        Random rand = new Random();
        for(int i = 1; i <= 48; i++) {
            if(i % 10 == 0) System.out.println(i + " finished, 48 in total");

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

            for(int k = 0; k < loopTimes4LoadFactor; k++) {
                // new random test cases
                int[] tests2 = new int[capacity / 100];
                for(int j = 0; j < tests2.length; j++) {
                    int tmp = rand.nextInt(capacity * 10);
                    while(set.contains(tmp)) {
                        tmp = rand.nextInt(capacity * 10);
                    }
                    tests2[j] = tmp;
                    set.add(tmp);
                }

                for(int q = 0; q < 4; q++) {
                    for(int p = 0; p < 3; p++) {
                        results[q][i - 1][p] += Operation(hashing[q], p,tests2);
                    }
                }
            }

            for(int q = 0; q < 4; q++) {
                for(int p = 0; p < 3; p++) {
                    results[q][i - 1][p] /= loopTimes4LoadFactor;
                }
            }
        }

        // print results
        for(long[][] result : results) {
            printResult(result);
        }
    }

    private static int Operation(Hashing hash, int type, int[] tests) {
        int count = 0;
        for(int test : tests) {
            if(type == 0) {
                count += hash.put(test, test);
            } else if(type == 1) {
                count += hash.get(test)[1];
            } else {
                count += hash.remove(test);
            }
        }
        return count;
    }

    private static void sequenceTest() {
        // to store test information
        long[][][] results = new long[4][testsNum][3];
        for (int k = 1; k <= testTimes; k++) {
            if (k % 20 == 0) {
                System.out.println(k + " times finished, " + testTimes + " in total");
            }

            // make random test cases
            int[] tests = new int[sampleNum];
            Random rand = new Random();
            HashSet<Integer> set = new HashSet<>();
            for (int i = 0; i < sampleNum; i++) {
                int test = rand.nextInt(capacity * 100);
                while (set.contains(test)) {
                    test = rand.nextInt(capacity * 100);
                }
                tests[i] = test;
            }

            for (int i = 1; i <= testsNum; i++) {
                Hashing[] hashing = new Hashing[4];
//                hashing[0] = new LinearHashing(capacity);
//                hashing[1] = new ChainedHashing(capacity);
                hashing[2] = new CuckooHashing(capacity);
//                hashing[3] = new QuadraticHashing(capacity);

//                for (int j = 0; j < 4; j++) {
//                    sum(results[j][i - 1], calculate(hashing[j], Arrays.copyOfRange(tests, 0, i * capacity / 50)));
//                }
                sum(results[2][i - 1], calculate(hashing[2], Arrays.copyOfRange(tests, 0, i * capacity / 50)));
            }
        }

//        for (int i = 0; i < 4; i++) {
//            printResult(mean(results[i], i));
//        }
        printResult(mean(results[2], 2));
    }

    private static void sum(long[] a1, long[] a2) {
        for(int i = 0; i < a1.length; i++) {
            a1[i] += a2[i];
        }
    }

    private static long[][] mean(long[][] a, int type) {
        long[][] res = new long[a.length][3];
        for(int i = 0; i < a.length; i++) {
            for(int j = 0; j < 3; j++) {
                res[i][j] = a[i][j] / testTimes;
            }
        }
        return res;
    }

    private static void printResult(long[][] results) {
        for(int i = 0; i < 3; i++) {
            for (int j = 0; j < testsNum; j++) {
                System.out.print(results[j][i] + ",");
            }
            System.out.println();
        }
    }

    private static long[] calculate(Hashing hashing, int[] tests) {
        long[] results = new long[3];
        // put
        for(int test : tests) {
            results[0] += hashing.put(test, test);
        }
        // get
        for(int test : tests) {
            results[1] += hashing.get(test)[1];
        }
        // remove
        for(int test : tests) {
            results[2] += hashing.remove(test);
        }
        return results;
    }
}
