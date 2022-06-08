// Example program
#include <iostream>
#include <string>

int main()
{
  std::pair <std::string,int> planet, homeplanet;

  planet = {"Earth",6371};

  homeplanet = planet;
  homeplanet.first = "hi";

  std::cout << "Home planet: " << homeplanet.first << '\n';
  std::cout << "Planet size: " << homeplanet.second << '\n';
}
