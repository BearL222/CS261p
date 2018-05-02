package Hashing;

import java.util.ArrayList;

public class QuadraticHashing extends Hashing {
    private ArrayList<Pair> list;
    private int capacity;


    public QuadraticHashing(int capacity) {
        list = new ArrayList<>(capacity);
        for(int i = 0; i < capacity; i++) {
            list.add(null);
        }
        this.capacity = capacity;
    }

    private int hashing(Integer key) {
        int result = key % capacity;
        return result;
    }


    public int put(Integer key, Integer value) {
        int count = 1;
        int hashVal = hashing(key);
        int index = (hashVal + count * count) % capacity;
        while(count < capacity + 1 && list.get(index) != null && list.get(index).key != null) {
            index = (hashVal + count * count) % capacity;
            count++;
        }
        if(count < capacity + 1) {
            list.set(index, new Pair(key, value));
            return 0;
        } else {
            return -1;
        }
    }


    public Integer get(Integer key) {
        int count = 1;
        int hashVal = hashing(key);
        int index = (hashVal + count * count) % capacity;
        while(count < capacity + 1 && list.get(index) != null && (list.get(index).key == null || !list.get(index).key.equals(key))) {
            index = (hashVal + count * count) % capacity;
            count++;
        }
        Integer result = null;
        if(count < capacity + 1 && list.get(index) != null) {
            result = list.get(index).value;
        }
        return result;
    }


    public int remove(Integer key) {
        int count = 1;
        int hashVal = hashing(key);
        int index = (hashVal + count * count) % capacity;
        while(count < capacity + 1 && list.get(index) != null && (list.get(index).key == null || !list.get(index).key.equals(key))) {
            index = (hashVal + count * count) % capacity;
            count++;
        }

        int result = 0;
        if(count >= capacity + 1 || list.get(index) == null) {
            result = -1;
        } else {
            list.get(index).key = null;
        }
        return result;
    }
}
