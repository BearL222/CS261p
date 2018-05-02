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
            return 0;
        } else {
            return -1;
        }
    }


    public Integer get(Integer key) {
        int index = hashing(key);
        int count = 0;
        while(count != capacity && list.get(index) != null && !list.get(index).key.equals(key)) {
            index = (index + 1) % capacity;
            count++;
        }
        Integer result = null;
        if(count != capacity && list.get(index) != null) {
            result = list.get(index).value;
        }
        return result;
    }


    public int remove(Integer key) {
        int index = hashing(key);
        int count = 0;
        while(count != capacity && list.get(index) != null && (list.get(index).key == null || !list.get(index).key.equals(key))) {
            index = (index + 1) % capacity;
            count++;
        }

        int result = 0;
        if(count == capacity || list.get(index) == null) {
            result = -1;
        } else {
            list.get(index).key = null;
        }
        return result;
    }
}
