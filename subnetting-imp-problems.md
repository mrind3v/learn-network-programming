## You asked:

how to solve questions where we are asked how many /27 subnets are inside /24 subnets?

---

## Gemini Replied:

A /24 network contains **8** /27 subnets.

The calculation is straightforward and relies on the difference between the two subnet prefixes.

***

### ## The Simple Math 🧠

The number in CIDR notation (like /24) tells you how many bits are used for the **network portion** of the address. The remaining bits are for the **host portion**.

1.  **/24 Network**: Uses **24 bits** for the network.
2.  **/27 Network**: Uses **27 bits** for the network.

To find how many smaller subnets fit into a larger one, you just find the difference in their prefix bits:

* **Difference** = (Bits in smaller subnet) - (Bits in larger network)
* Difference = $27 - 24 = 3$ bits

This means you are using **3 extra bits** from the host portion of the /24 network to create the smaller /27 subnets.

With 3 bits, you can create $2^3$ possible combinations:
$$2^3 = 8$$
So, you can create **8 unique /27 subnets**.

***

### ## Why This Works: A Visual Breakdown

Let's use the example network `192.168.0.0/24`.

#### The /24 Network

The first 24 bits (3 octets) are fixed as the network address. The last 8 bits are for hosts.

* **Network**: `11000000.10101000.00000000` (`192.168.0`)
* **Hosts**: `hhhhhhhh` (The last 8 bits, from `.0` to `.255`)

#### Subnetting into /27s

We "borrow" 3 bits from the host part to use for our new subnets. The last octet now looks like this:

`sss hhhhh`

* The first 3 bits (`sss`) identify the **subnet**.
* The last 5 bits (`hhhhh`) identify the **hosts** within that subnet.

Let's list the 8 possible combinations for the `sss` bits and see what subnets they create:

| Subnet Bits (`sss`) | Decimal Value | Resulting /27 Subnet |
| :--- | :--- | :--- |
| `000` | 0 | `192.168.0.0/27` |
| `001` | 32 | `192.168.0.32/27` |
| `010` | 64 | `192.168.0.64/27` |
| `011` | 96 | `192.168.0.96/27` |
| `100` | 128 | `192.168.0.128/27` |
| `101` | 160 | `192.168.0.160/27` |
| `110` | 192 | `192.168.0.192/27` |
| `111` | 224 | `192.168.0.224/27` |

As you can see, the 3 borrowed bits give us exactly 8 unique subnets.

***

### ## General Formula ✅

You can use this formula for any similar question.

Given a larger network `/N` and a smaller subnet `/M`:

**Number of `/M` subnets inside a `/N` network = $2^{(M - N)}$**

**Example**: How many /30 subnets are in a /26 network?
* Difference = $30 - 26 = 4$
* Number of subnets = $2^4 = 16$