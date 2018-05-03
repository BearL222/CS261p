package Hashing;

import java.util.ArrayList;
import java.util.Random;

public class CuckooHashing extends Hashing {
    int resizeNum = 0;
    int capacity;
    int c4Resize;
    ArrayList<ArrayList<Pair>> list;
    int magicNumRange = 1000;
    int magicHashNum1;
    int magicHashNum2;

    CuckooHashing(int capacity) {
        this.c4Resize = 30;
        this.capacity = capacity;
        newHashFunc();
        list = new ArrayList<>();
        list.add(new ArrayList<Pair>());
        list.add(new ArrayList<Pair>());

        for(int i = 0; i < capacity; i++) {
            list.get(0).add(null);
            list.get(1).add(null);
        }
    }

    private void newHashFunc() {
        Random rand = new Random();
        magicHashNum1 = rand.nextInt(magicNumRange) + 1;
        magicHashNum2 = rand.nextInt(magicNumRange) + 1;
        while(magicHashNum2 == magicHashNum1) {
            magicHashNum2 = rand.nextInt(magicNumRange) + 1;
        }
    }


    private int hashing(int function, Integer key) {
        int result = 0;
        if(function == 0) {
            result = (key + magicHashNum1) % capacity;
        } else {
            result = ((key + magicHashNum2) / capacity) % capacity;
        }
        return result;
    }


    public int put(Integer key, Integer value) {
        Pair toPut = new Pair(key, value);
        int count = 0;
        int[] result = findPlace(toPut);
        count += result[4];
        if(result[0] == -1) {
            count += resize(new Pair(result[2],result[3]));
        } else {
            list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
            count++;
        }
        return count;
    }

    private int[] findPlace(Pair toPut) {
        Pair origin = toPut;
        int t = 0;
        int count = 0;
        int index = hashing(t, toPut.key);
        boolean alreadyExist = false;
        while(list.get(t).get(index) != null && count < c4Resize * Math.log10(capacity)) {
            if(list.get(t).get(index).key == origin.key && list.get(t).get(index) != origin) {
                alreadyExist = true;
                break;
            }

            count++;
            Pair tmp = toPut;
            toPut = list.get(t).get(index);
            list.get(t).set(index, tmp);

            t = 1 - t;
            index = hashing(t, toPut.key);
        }

        int[] result;
        if(list.get(t).get(index) == null || alreadyExist) {
            result = new int[]{t, index, toPut.key, toPut.value, count};
        } else {
            result = new int[]{-1, -1, toPut.key, toPut.value, count};
        }
        return result;
    }

    private int resize(Pair toPut) {
        resizeNum++;
        ArrayList<ArrayList<Pair>> backupList = this.list;
        boolean noConflict;
        int count = 0;
        int newHashCount = 0;
        do {
            noConflict = true;
            if(newHashCount < 10) {
                newHashFunc();
                newHashCount++;
            } else {
                capacity *= 2;
                newHashCount = 0;
            }
            // prepare a new array list
            ArrayList<ArrayList<Pair>> newList = new ArrayList<>();
            newList.add(new ArrayList<>());
            newList.add(new ArrayList<>());
            for(int i = 0; i < capacity; i++) {
                newList.get(0).add(null);
                newList.get(1).add(null);
                count += 2;
            }

            this.list = newList;
            int[] result;

            for(int i = 0; i < 2; i++) {
                for(Pair pair : backupList.get(i)) {
                    if(pair == null) continue;
                    result = findPlace(new Pair(pair.key, pair.value));
                    count += result[4];
                    if(result[0] == -1) {
                        noConflict = false;
                        break;
                    } else {
                        list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
                        count++;
                    }
                }
                if(!noConflict) break;
            }
            if(noConflict) {
                result = findPlace(toPut);
                count += result[4];
                if(result[0] == -1) {
                    noConflict = false;
                } else {
                    list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
                    count++;
                }
            }
        } while(!noConflict);

        return count;
    }

    public int[] get(Integer key) {
        int result = -1;
        int count = 0;
        for(int i = 0; i < 2; i++) {
            count++;
            int index = hashing(i, key);
            if (list.get(i).get(index) != null && list.get(i).get(index).key.equals(key)) {
                result = list.get(i).get(index).value;
                break;
            }
        }
        return new int[]{result, count};
    }

    public int remove(Integer key) {
        int count = 0;
        for(int i = 0; i < 2; i++) {
            count++;
            int index = hashing(i, key);
            if (list.get(i).get(index) != null && list.get(i).get(index).key.equals(key)) {
                list.get(i).set(index, null);
            }
        }
        return count;
    }
}
