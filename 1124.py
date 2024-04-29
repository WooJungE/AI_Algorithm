//17202. 핸드폰 번호 궁합

#include <iostream>
#include <string>
using namespace std;

int main() {
	string n1, n2;
	string add; // 두 문자열의 각 자리 숫자를 합한 결과를 저장할 변수
	string res; // 각 단계에서의 합산 결과를 임시 저장할 변수

	// 사용자로부터 두 문자열 입력 받기
	cin >> n1;
	cin >> n2;

	// 첫 번째 문자열의 크기만큼 반복
	for (int i = 0; i < n1.size(); i++) {
	    // n1과 n2의 각 자리 숫자를 합하여 add 문자열에 추가
		add = add + n1[i] + n2[i];
	}

	// add 문자열의 크기가 2가 될 때까지 반복
	while (add.size() != 2) {
	    // add 문자열의 크기 - 1만큼 반복
		for (int i = 0; i < add.size() - 1; i++) {
		    // 현재 자리 숫자와 다음 자리 숫자를 합한 후, 10으로 나눈 나머지를 res 문자열에 추가
			res = res + char('0' + ((add[i] - '0') + (add[i + 1] - '0')) % 10); 
		}
		// 다음 단계를 위해 add를 res로 업데이트하고, res를 초기화
		add = res;
		res.clear(); 
	}

	// 최종적으로 남은 두 자리 숫자 출력
	cout << add;
}
