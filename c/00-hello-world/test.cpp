#define CATCH_CONFIG_MAIN
#include "catch.hpp"

unsigned int squarings (unsigned int x)
{
    return x * x;
}

TEST_CASE("Squaring are computed", "[squarings]") {
    REQUIRE( squarings(1) == 1);
    REQUIRE( squarings(2) == 2);
}
