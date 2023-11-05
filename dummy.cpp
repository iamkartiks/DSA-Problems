#include<iostream>

int method(int n){
    int result = n * n;
    return result;
}

int main(){
    int number;
    std::cout<<"Give number :\n";
    std::cin>>number;

    int value = method(number);
    std::cout<<"Result is:"<<value<<"\n";
}