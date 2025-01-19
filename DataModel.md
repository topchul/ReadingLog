# DataModel

| 필드명                 | 자료형/설명                                          |
|-----------------------|------------------------------------------------------|
| 제목(title)            | 문자열                                               |
| 부제(subtitle)         | 문자열 (없을 수도 있음)                               |
| 저자(author)           | 문자열 (1명 이상)                                     |
| 링크(link)             | 문자열 (구매/상세정보 URL 등)                          |
| 현재상태(status)       | 문자열 (예: ‘읽는 중’, ‘시작 전’, ‘완료’, ‘중단’ 등)    |
| 트리거(trigger)        | 문자열 (이 책을 알게 된 경로)                          |
| 별점(rating)           | 정수(1~5) 혹은 0~5                                   |
| 완료일(completed_date) | 날짜(datetime.date). 완료 상태일 때만 유효.            |
| 유형(book_type)        | 문자열 (종이책, 전자책, 오디오북 등)                   |
| 생성일시(created_at)   | 날짜시간(datetime)                                    |
| 수정일시(updated_at)   | 날짜시간(datetime)                                    |
| 표지(cover_image)      | 이미지 파일 경로/URL. 로컬 파일 저장 or DB BLOB(권장X)  |
| 메모(memo)             | markdown 형식의 문자열                                |
