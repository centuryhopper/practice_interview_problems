#include <map>
#include <iostream>
#define p(x) std::cout << std::to_string(x) << "\n"

template <
    class Key,
    class Value,
    class Comparator = typename std::map<Key, Value>::key_compare,
    class Allocator = typename std::map<Key, Value>::allocator_type>
class DefaultDict : private std::map<Key, Value, Comparator, Allocator>
{
public:
  // Publish the clear() function as is
  using std::map<Key, Value, Comparator, Allocator>::clear;

  // Provide my own at()
  Value &at(const Key &key)
  {
    return std::map<Key, Value, Comparator, Allocator>::operator[](key); //call the inherited function
  }

  // Etc.
};

int main(int argc, char const *argv[])
{
  DefaultDict<int, int> m;
  p(m.at(0));

  return 0;
}
