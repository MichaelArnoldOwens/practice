/* 
Many shopping websites today provide a "co-buy suggestion" feature. For example, when you look at a laptop, the website can also suggest a monitor, a keyboard, etc.

Let's make a simple implementation that can generate product suggestions. We will want the following features:

- ability to record purchases consisting of multiple products.
- given a product name (eg "laptop") return the top 3 other product names that people have frequently bought together (ie other products purchased along with a Laptop).

{
  monitor: {
    items_dict: {mouse: {count: number }, ssd: {count: }}
  },
  mouse: {
    ...
  }
}

monitor, mouse, ssd

checkout(cart)

monitor:
[{
  name
  times_it_was_bought
}, ...]

fbw: topThreeFbw(name: string) => [product1, product2, product3]

node
  - product name
  -
*/

const products_bought_count = {}

const initialize_product_count_object = (other_products) => {
  console.log('other_products', other_products)
  const product_neighbor_count = {}
  other_products.forEach(p => { product_neighbor_count[p] = 1 })
  return product_neighbor_count
}

// # ['monitor', 'keyboard', 'mouse']
function checkout(cart) {
  for (const product of cart) {
    if (product in products_bought_count) {
      const product_neighbor_count = products_bought_count[product]
      const other_products = cart.filter(p => p !== product)
      other_products.forEach(p => {
        if (p in product_neighbor_count) {
          product_neighbor_count[p] += 1
        } else {
          product_neighbor_count[p] = 1
        }
      })
    } else {
      const other_products = cart.filter(p => p !== product)
      const product_neighbor_count = initialize_product_count_object(other_products)
      products_bought_count[product] = product_neighbor_count
    }
  }
  console.log(products_bought_count)
  return products_bought_count
}

function getTopThreeFbw(product) {
  const product_neighbor_count = products_bought_count[product]
  console.log(product_neighbor_count)
  if (!product_neighbor_count) return []
  const sorted_product_count_list = Object.entries(product_neighbor_count).sort((a, b) => {
    return b[1] - a[1]
  })
  console.log('sorted:', sorted_product_count_list)
  return sorted_product_count_list.slice(0, 3).map(x => x[0])
}

console.log(checkout(['monitor', 'keyboard', 'mouse', 'game']))
console.log(checkout(['monitor', 'keyboard', 'mouse']))
console.log(checkout(['monitor', 'game', 'camera']))
console.log(checkout(['monitor', 'game', 'camera']))
console.log(checkout(['monitor', 'game']))
console.log(checkout(['game', 'mouse', 'monitor']))
checkout(['ssd', 'hdd', 'camera'])

console.log(getTopThreeFbw('monitor'))
console.log(getTopThreeFbw('game'))
console.log(getTopThreeFbw('camera'))

