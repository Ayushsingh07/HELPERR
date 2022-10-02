import java.util.Date;

public class Block {
    int index, proof;
    Date timestamp;
    String prev_hash, data;

    public Block(int index, int proof, Date timestamp, String prev_hash, String data){
        this.index = index;
        this.proof = proof;
        this.timestamp = timestamp;
        this.data = data;
        this.prev_hash = prev_hash;
    }

    public int getIndex() {
        return index;
    }

    public int getProof() {
        return proof;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public String getPrev_hash() {
        return prev_hash;
    }

    public String getData() {
        return data;
    }
}
