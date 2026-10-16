#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
void process_audio(std::vector<float>& b, float gain) {
    for (size_t i = 0; i < b.size(); ++i) b[i] = std::tanh(b[i] * gain);
}
int main() {
    std::vector<float> a(44100 * 5, 0.75f);
    auto t0 = std::chrono::high_resolution_clock::now();
    process_audio(a, 1.5f);
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << "[ABYSSAL-CORE] 5s de audio en "
              << std::chrono::duration<double, std::milli>(t1 - t0).count() << " ms" << std::endl;
}
