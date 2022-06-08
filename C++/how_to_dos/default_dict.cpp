#include "../templates/template.h"

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

    // overload []
    Value &operator[](const Key &key)
    {
        return std::map<Key, Value, Comparator, Allocator>::operator[](key);
    }

    // Etc.
};

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;
    DefaultDict<int, char> m;
    cout<<(m[44] == '\0')<<endl;
    return 0;
}
