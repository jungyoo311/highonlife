#include <iostream>
using namespace std;

// Main Base Class Animal
class Animal {
    public:
    virtual void speak() {
        cout << "Animal makes a sound" << endl;
    }
};

// Dog class will inherit base class
class Dog : public Animal{
    public:
    void speak() override {
        cout << "Bark" << endl;
    }
};

// Cow class will inheriet base class
class Cow : public Animal {
    void speak() override {
        cout << "MOO" << endl;
    }
};

int main() {
    Animal* ptrDog = new Dog();
    Animal* ptrCow = new Cow();

    // Call inherited classes
    ptrDog->speak();
    ptrCow->speak();

    // memory deallocation: this is the process of returning memory to the system after it is no longer needed. The delete operate performs this task
    delete ptrDog;
    delete ptrCow;
    
    return 0;
}
