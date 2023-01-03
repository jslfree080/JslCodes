package dP;

import java.util.ArrayList;

interface PayMethod {
    void pay(int amountP);
}

class CreditCard implements PayMethod {

    private String name;
    private long cardNumber;
    private String cvv;
    private String dateOfExpiry;

    CreditCard(String nm, long cN, String cvvP, String dOE) {
        name = nm;
        cardNumber = cN;
        cvv = cvvP;
        dateOfExpiry = dOE;
    }

    @Override
    public void pay(int amountP) {
        System.out.println(amountP + " paid using credit/debit card.");
    }
}

class Paypal implements PayMethod {

    private String mail;
    private String password;

    Paypal(String mailP, String pwd) {
        mail = mailP;
        password = pwd;
    }

    @Override
    public void pay(int amountP) {
        System.out.println(amountP + " paid with Paypal.");
    }
}

enum Size {

    S(1), L(2), XL(3);

    private int sizeInt;

    Size(int sizeP) {
        this.sizeInt = sizeP;
    }

    @Override
    public String toString() {
        switch(sizeInt) {
            case 1:
                return "small";
            case 2:
                return "large";
            case 3:
                return "extra large";
            default:
                return "CUSTOM";
        }
    }

}

class Item {

    private Size size;
    private int price;

    Item(Size sizeP, int priceP) {
        size = sizeP;
        price = priceP;
    }

    public int getPrice() {
        return price;
    }
}

public class PayItems {

    private ArrayList<Item> items = new ArrayList<>();

    public void addItem(Item itemP) {
        items.add(itemP);
    }
    public void removeItem(Item itemP) {
        items.remove(itemP);
    }
    public int calculateTotal() {
        int sum = 0;
        for(Item itemP : items) {
            sum += itemP.getPrice();
        }
        return sum;
    }
    public void runPayMethod(PayMethod paymethodP) {
        int amount = calculateTotal();
        paymethodP.pay(amount);
    }

    public static void main(String[] args) throws Exception {
        PayItems pi = new PayItems();
        Item item1 = new Item(Size.S, 20);
        Item item2 = new Item(Size.L, 30);
        Item item3 = new Item(Size.XL, 100);
        pi.addItem(item1);
        pi.addItem(item2);
        pi.runPayMethod(new Paypal("jslfree080@gmail.com", "somePassword"));
        pi.removeItem(item1);
        pi.removeItem(item2);
        pi.addItem(item3);
        pi.runPayMethod(new CreditCard("Jungsoo Lee", 12345678901234L, "080", "12/12"));
    }
}