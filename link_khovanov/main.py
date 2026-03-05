import javakh_interface
import pd_code_reverse_component
import pd_code_sanity
import pd_code_components

import json

def link_khovanov(pd_code:list[list]) -> list[str]:

    # 检查 pd_code 合法性
    if not pd_code_sanity.sanity(pd_code):
        raise TypeError()

    pd_components = pd_code_components.get_components_from_pd_code(pd_code)
    n_components = len(pd_components)

    # 记录所有 khovanov 同调
    khovanov_list = []

    # 枚举所有可能定向
    for index in range(1<<n_components):
        binary_arr = [
            (index >> i) & 1
            for i in range(n_components)
        ]
        assert len(binary_arr) == len(pd_components)

        new_pd_code = json.loads(json.dumps(pd_code))
        for i in range(len(pd_components)):
            if binary_arr[i]:
                new_pd_code = pd_code_reverse_component.reverse_component(new_pd_code,
                    pd_components[i][0])
        
        new_khovanov = javakh_interface.solve_khovanov(new_pd_code)
        khovanov_list.append(new_khovanov)
    
    return list(set(sorted(khovanov_list)))

if __name__ == "__main__":
    pd_code = [[10, 1, 11, 2], [12, 3, 13, 4], [14, 19, 15, 20], [18, 7, 19, 8], [16, 5, 17, 6], [4, 15, 5, 16], [6, 17, 7, 18], [20, 13, 9, 14], [2, 9, 3, 10], [8, 11, 1, 12]]
    for idx, line in enumerate(link_khovanov(pd_code)):
        print(f"{idx:02d}", line, "\n")
