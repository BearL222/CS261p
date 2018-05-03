package Hashing;

import java.util.Arrays;
import java.util.Random;

public class Main {
    static int capacity = 5000;
    static int testsNum = 48;
    static int testTimes = 300;
    static int loopTimes4LoadFactor = 100;

    public static void main(String[] args) {
//        sequenceTest();
        diffLoadFactor();
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
            for(int j = 0; j < tests.length; j++) {
                int tmp = rand.nextInt(Integer.MAX_VALUE - 1000);
                tests[i] = tmp;
                for(Hashing hash : hashing) {
                    hash.put(tmp, tmp);
                }
            }

            for(int k = 0; k < loopTimes4LoadFactor; k++) {
                // new random test cases
                int[] tests2 = new int[capacity / 100];
                for(int j = 0; j < tests2.length; j++) {
                    int tmp = rand.nextInt(Integer.MAX_VALUE - 1000);
                    tests2[j] = tmp;
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
        testsNum = (int)(testsNum * 1.1);

        // to store test information
        long[][] results = new long[testsNum][3];
        int maxCapacity = capacity * testsNum / 50;
        int[] tests = new int[maxCapacity];
        Random rand = new Random();

        for (int k = 1; k <= testTimes; k++) {
            if (k % 10 == 0) {
                System.out.println(k + " times finished, " + testTimes + " in total");
            }

            // make random test cases
            for (int i = 0; i < maxCapacity; i++) {
                int test = rand.nextInt(Integer.MAX_VALUE - 1000);
                tests[i] = test;
            }

            for (int i = 1; i <= testsNum; i++) {
                sum(results[i - 1], calculate(Arrays.copyOfRange(tests, 0, i * capacity / 50)));
            }
        }

        printResult(mean(results, 2));
    }

    private static void sum(long[] a1, long[] a2) {
        for(int i = 0; i < a1.length; i++) {
            a1[i] += a2[i];
        }
    }

    private static long[][] mean(long[][] a, int type) {
        long[][] res = new long[a.length][a[0].length];
        for(int i = 0; i < a.length; i++) {
            for(int j = 0; j < a[0].length; j++) {
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

    private static long[] calculate(int[] tests) {
        long[] results = new long[3];
        CuckooHashing hashing = new CuckooHashing(capacity);

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
