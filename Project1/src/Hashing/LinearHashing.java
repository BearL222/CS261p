package Hashing;

import java.util.ArrayList;

public class LinearHashing extends Hashing {
    private ArrayList<Pair> list;
    private int capacity;


    public LinearHashing(int capacity) {
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
        int index = hashing(key);
        int count = 0;
        while(count != capacity && list.get(index) != null && list.get(index).key != null) {
            index = (index + 1) % capacity;
            count++;
        }
        if(count != capacity) {
            list.set(index, new Pair(key, value));
            count++;
        }
        return count;
    }


    public int[] get(Integer key) {
        int index = hashing(key);
        int count = 0;
        while(count != capacity && list.get(index) != null && !list.get(index).key.equals(key)) {
            index = (index + 1) % capacity;
            count++;
        }
        int result = -1;
        if(count != capacity && list.get(index) != null) {
            result = list.get(index).value;
        }
        return new int[]{result, count};
    }


    public int remove(Integer key) {
        int index = hashing(key);
        int count = 0;
        while(count != capacity && list.get(index) != null && (list.get(index).key == null || !list.get(index).key.equals(key))) {
            index = (index + 1) % capacity;
            count++;
        }

        if(count != capacity && list.get(index) != null) {
            list.get(index).key = null;
            count++;
        }
        return count;
    }
}
