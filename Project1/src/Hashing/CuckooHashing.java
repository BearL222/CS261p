package Hashing;

import java.util.ArrayList;

public class CuckooHashing extends Hashing {
    int capacity;
    int c4Resize;
    ArrayList<ArrayList<Pair>> list;

    CuckooHashing(int capacity) {
        this.c4Resize = 100;
        this.capacity = capacity;
        list = new ArrayList<>();
        list.add(new ArrayList<Pair>());
        list.add(new ArrayList<Pair>());

        for(int i = 0; i < capacity; i++) {
            list.get(0).add(null);
            list.get(1).add(null);
        }
    }


    private int hashing(int function, Integer key) {
        int result = 0;
        if(function == 0) {
            result = key % capacity;
        } else {
            result = (key / capacity) % capacity;
        }
        return result;
    }


    public int put(Integer key, Integer value) {
        Pair toPut = new Pair(key, value);
        int[] result = findPlace(toPut);
        if(result[0] == -1) {
            resize(new Pair(result[2],result[3]));
        } else {
            list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
        }
        return 0;
    }

    private int[] findPlace(Pair toPut) {
        int t = 0;
        int count = 0;
        int index = hashing(t, toPut.key);
        while(list.get(t).get(index) != null && count < capacity) {
            // if new put key is the same with already existing one
            if(list.get(t).get(index).key.equals(toPut.key)) {
                break;
            }

            Pair tmp = toPut;
            toPut = list.get(t).get(index);
            list.get(t).set(index, tmp);

            t = 1 - t;
            index = hashing(t, toPut.key);
            count++;
        }

        int[] result;
        if(count >= capacity) {
            result = new int[]{-1, -1, toPut.key, toPut.value};
        } else {
            result = new int[]{t, index, toPut.key, toPut.value};
        }
        return result;
    }

    private void resize(Pair toPut) {
        ArrayList<ArrayList<Pair>> backupList = this.list;
        boolean noConflict;
        do {
            noConflict = true;
            capacity *= 2;
            // prepare a new array list
            ArrayList<ArrayList<Pair>> newList = new ArrayList<>();
            newList.add(new ArrayList<>());
            newList.add(new ArrayList<>());
            for(int i = 0; i < capacity; i++) {
                newList.get(0).add(null);
                newList.get(1).add(null);
            }

            this.list = newList;
            int[] result;

            for(int i = 0; i < 2; i++) {
                for(Pair pair : backupList.get(i)) {
                    if(pair == null) continue;
                    result = findPlace(new Pair(pair.key, pair.value));
                    if(result[0] == -1) {
                        noConflict = false;
                        break;
                    } else {
                        list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
                    }
                }
                if(!noConflict) break;
            }
            if(noConflict) {
                result = findPlace(toPut);
                if(result[0] == -1) {
                    noConflict = false;
                } else {
                    list.get(result[0]).set(result[1], new Pair(result[2], result[3]));
                }
            }
        } while(!noConflict);
    }

    public Integer get(Integer key) {
        for(int i = 0; i < 2; i++) {
            int index = hashing(i, key);
            if (list.get(i).get(index) != null && list.get(i).get(index).key.equals(key)) {
                return list.get(i).get(index).value;
            }
        }
        return null;
    }

    public int remove(Integer key) {
        for(int i = 0; i < 2; i++) {
            int index = hashing(i, key);
            if (list.get(i).get(index) != null && list.get(i).get(index).key.equals(key)) {
                list.get(i).set(index, null);
            }
        }
        return 0;
    }
}
