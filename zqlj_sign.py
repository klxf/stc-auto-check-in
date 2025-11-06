import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def visit_url_and_sign(base_url, index_url, cookies_str, output_filename="zqlj_sign.html"):
    headers = {
        "Cookie": cookies_str,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    print(f"正在访问打卡首页: {index_url}")
    try:
        response = requests.get(index_url, headers=headers)
        print(f"请求状态码: {response.status_code}")

        if response.status_code == 200:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"响应内容已成功缓存到 '{output_filename}'")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            sign_div = soup.find('div', class_='bm signbtn cl')
            sign_link_tag = None
            if sign_div:
                sign_link_tag = sign_div.find('a', class_='btna')

            if sign_link_tag and 'href' in sign_link_tag.attrs:
                relative_href = sign_link_tag['href']
                full_sign_url = urljoin(base_url, relative_href)
                print("\n--- 找到打卡链接 ---")
                print(full_sign_url)
                print("--------------------\n")

                print(f"请求打卡链接: {full_sign_url}")
                sign_response = requests.get(full_sign_url, headers=headers)
                print(f"请求状态码: {sign_response.status_code}")

                if sign_response.status_code == 200:
                    print("成功请求打卡链接！")
                    sign_result_soup = BeautifulSoup(sign_response.text, 'html.parser')
                    message_div = sign_result_soup.find('div', id='messagetext')

                    if message_div:
                        message_text = message_div.get_text(strip=True) # 获取并去除空白字符
                        print("\n--- 打卡结果消息 ---")
                        print(message_text)
                        print("--------------------\n")
                    else:
                        print("在打卡结果页面中未找到 ID 为 'messagetext' 的 div 元素。请查看")
                else:
                    print("打卡请求失败。")
                    print("\n--- 请求响应内容 ---")
                    print(sign_response.text[:500])

            else:
                print("未找到 '点击打卡' 链接或其 href 属性。请检查页面内容是否已更新或已打卡。")

        else:
            print(f"初始访问失败，状态码为 {response.status_code}。无法进行打卡操作。")
            print("\n--- 请求响应内容 ---")
            print(response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
    except AttributeError:
        print("解析HTML时出现错误，未找到目标元素")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    base_url = "https://www.stcaimcu.com/"
    index_target_url = "https://www.stcaimcu.com/plugin.php?id=zqlj_sign"
  
    cookies_str = os.getenv('STCAIMCU_Cookies')
    print("========== STC论坛签到[开始] ==========")
    
    if not cookies_str:
        print("错误：未找到 'STCAIMCU_Cookies' 环境变量，确保已在 GitHub Actions 中设置 Secret")
    else:
        visit_url_and_sign(base_url, index_target_url, cookies_str)

    print("========== STC论坛签到[结束] ==========")
