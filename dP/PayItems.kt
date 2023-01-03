interface PayMethod {
    fun pay(amountP: Int)
}

class CreditCard(
    private val name: String,
    private val cardNumber: Long,
    private val cvv: String,
    private val dateOfExpiry: String
) : PayMethod {
    override fun pay(amountP: Int) {
        println("$amountP paid using credit/debit card.")
    }
}

class Paypal(private val mail: String, private val password: String) : PayMethod {
    override fun pay(amountP: Int) {
        println("$amountP paid with Paypal.")
    }
}

enum class Size(private val sizeInt: Int) {
    S(1), L(2), XL(3);

    override fun toString(): String {
        return when (sizeInt) {
            1 -> "small"
            2 -> "large"
            3 -> "extra large"
            else -> "CUSTOM"
        }
    }
}

class Item(private val size: Size, private val price: Int) {
    fun getPrice(): Int {
        return price
    }
}

class PayItems {
    private val items = mutableListOf<Item>()

    fun addItem(itemP: Item) {
        items.add(itemP)
    }
    fun removeItem(itemP: Item) {
        items.remove(itemP)
    }
    fun calculateTotal(): Int {
        var sum = 0
        for (itemP in items) {
            sum += itemP.getPrice()
        }
        return sum
    }
    fun runPayMethod(paymethodP: PayMethod) {
        val amount = calculateTotal()
        paymethodP.pay(amount)
    }
}

fun main() {
    val pi = PayItems()
    val item1 = Item(Size.S, 20)
    val item2 = Item(Size.L, 30)
    val item3 = Item(Size.XL, 100)
    pi.addItem(item1)
    pi.addItem(item2)
    pi.runPayMethod(Paypal("jslfree080@gmail.com", "somePassword"))
    pi.removeItem(item1)
    pi.removeItem(item2)
    pi.addItem(item3)
    pi.runPayMethod(CreditCard("Jungsoo Lee", 12345678901234L, "080", "12/12"))
}