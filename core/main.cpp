#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    std::cout << "🔥 [AEROCORE-X] C++20 SIMD + OMP Activo" << std::endl;
    std::vector<float> buffer(1024, 1.0f);
    #pragma omp parallel for
    for (size_t i = 0; i < buffer.size(); ++i) {
        buffer[i] *= 2.0f;
    }
    std::cout << "✅ Inferencia SIMD completada. Control: " << buffer[0] << std::endl;
    return 0;
}
