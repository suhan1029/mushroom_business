import streamlit as st
from PIL import Image
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

# Load environment variables
load_dotenv()

# Email sending function
def send_email(name, sender_email, category, message):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")
    
    if not sender or not password or not receiver:
        return False, "이메일 설정이 완료되지 않았습니다. (.env 파일을 확인해주세요)"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = f"[버컵 문의] {category} - {name}님"
    
    body = f"""
    버컵 홈페이지를 통해 새로운 문의가 접수되었습니다.
    
    - 성함/업체명: {name}
    - 이메일: {sender_email}
    - 문의유형: {category}
    
    [상세 내용]
    {message}
    """
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return True, "성공"
    except Exception as e:
        return False, str(e)

# Page configuration
st.set_page_config(
    page_title="버컵 (Vercup) - 친환경 버섯 폐배지 컵홀더",
    page_icon="🍄",
    layout="wide"
)

# Load images
def load_image(img_name):
    path = os.path.join(os.getcwd(), img_name)
    if os.path.exists(path):
        return Image.open(path)
    return None

logo = load_image("Vercup.png")
promo1 = load_image("Vercup_1.png")
promo2 = load_image("Vercup_2.png")

# Custom CSS for better UI (Light/Dark mode compatible)
st.markdown("""
    <style>
    /* Hero text with theme-aware colors */
    .hero-text {
        font-size: 3rem;
        font-weight: 800;
        color: #2E7D32; /* Forest Green - works in both */
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .sub-hero-text {
        font-size: 1.5rem;
        color: #43A047;
        margin-bottom: 2rem;
    }

    /* Card styling that adapts to theme */
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* Metric styling */
    [data-testid="stMetricValue"] {
        color: #2E7D32 !important;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(46, 125, 50, 0.05);
        border-radius: 10px 10px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        border: 1px solid rgba(46, 125, 50, 0.1);
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(46, 125, 50, 0.2) !important;
        border-bottom: 3px solid #2E7D32 !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(46, 125, 50, 0.1);
        color: #2E7D32;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    if logo:
        st.image(logo, width='stretch')
    else:
        st.title("🍄 버컵 (Vercup)")
    
    st.markdown("---")
    
    # Theme-aware option menu
    menu = option_menu(
        menu_title="메인 메뉴",
        options=["홈", "제품 소개", "비즈니스 모델", "Q&A", "파트너십"],
        icons=["house", "box-seam", "briefcase", "question-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "transparent"},
            "icon": {"color": "#4CAF50", "font-size": "20px"}, 
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin":"0px", 
                "--hover-color": "rgba(128, 128, 128, 0.2)"
            },
            "nav-link-selected": {"background-color": "#2E7D32"},
        }
    )

# Home Section
if menu == "홈":
    st.container()
    
    # Hero Section with a more modern look
    st.markdown("""
        <div style="
            text-align: center; 
            padding: 3rem 1rem; 
            background: rgba(46, 125, 50, 0.05); 
            border-radius: 20px; 
            margin-bottom: 3rem;
            border: 1px solid rgba(46, 125, 50, 0.1);
        ">
            <h1 style="font-size: 3.5rem; color: #2E7D32; margin-bottom: 0.5rem;">버섯 폐배지의 놀라운 변신</h1>
            <h2 style="font-size: 1.8rem; color: #43A047; font-weight: 400; margin-bottom: 2rem;">지속 가능한 미래를 위한 친환경 솔루션, <b>버컵(Vercup)</b></h2>
            <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.6; opacity: 0.8;">
                우리는 버려지는 자원에 새로운 가치를 부여합니다. 종이 사용을 줄이고 환경을 보호하며, 
                카페 운영의 효율성을 높이는 혁신적인 버섯 폐배지 컵홀더를 만나보세요.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("### 🌱 Why Vercup?")
        st.write("")
        
        # Value Propositions as cards
        value_props = [
            ("♻️", "100% 업사이클링", "버려지는 버섯 폐배지를 주원료로 사용하여 자원 순환을 실천합니다."),
            ("📉", "획기적인 비용 절감", "원료비 0원에 도전하여 기존 종이 홀더 대비 높은 경제성을 제공합니다."),
            ("🌡️", "탁월한 단열 성능", "균사체의 다공성 구조가 열을 효과적으로 차단하여 안전합니다.")
        ]
        
        for icon, title, desc in value_props:
            st.markdown(f"""
                <div style="margin-bottom: 1.5rem;">
                    <span style="font-size: 1.5rem;">{icon}</span>
                    <b style="font-size: 1.1rem; color: #2E7D32; margin-left: 10px;">{title}</b>
                    <p style="margin-left: 35px; font-size: 0.95rem; opacity: 0.8;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        if promo1:
            st.image(promo1, width='stretch')
            st.caption("버컵(Vercup) - 자연에서 와서 자연으로 돌아가는 기술")

    st.write("")
    st.divider()
    
    st.markdown("<h3 style='text-align: center; margin-bottom: 2rem;'>📊 버컵의 임팩트</h3>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
            <div style="text-align: center; padding: 1rem; border-radius: 15px; background: rgba(46, 125, 50, 0.03);">
                <p style="font-size: 0.9rem; margin-bottom: 0;">친환경 지수</p>
                <h2 style="color: #2E7D32; margin-top: 0;">100%</h2>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div style="text-align: center; padding: 1rem; border-radius: 15px; background: rgba(46, 125, 50, 0.03);">
                <p style="font-size: 0.9rem; margin-bottom: 0;">생분해 기간</p>
                <h2 style="color: #2E7D32; margin-top: 0;">45일</h2>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
            <div style="text-align: center; padding: 1rem; border-radius: 15px; background: rgba(46, 125, 50, 0.03);">
                <p style="font-size: 0.9rem; margin-bottom: 0;">생산 원가</p>
                <h2 style="color: #2E7D32; margin-top: 0;">-90%</h2>
            </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
            <div style="text-align: center; padding: 1rem; border-radius: 15px; background: rgba(46, 125, 50, 0.03);">
                <p style="font-size: 0.9rem; margin-bottom: 0;">단열 성능</p>
                <h2 style="color: #2E7D32; margin-top: 0;">Best</h2>
            </div>
        """, unsafe_allow_html=True)

# Product Section
elif menu == "제품 소개":
    st.title("🍄 제품 상세 정보")
    st.markdown("버컵의 혁신적인 기술과 체계적인 생산 공정을 소개합니다.")
    
    tab1, tab2, tab3 = st.tabs(["✨ 주요 특징", "⚙️ 제조 공정", "📊 SWOT 분석"])
    
    with tab1:
        st.write("")
        col1, col2 = st.columns([1, 1.2], gap="large")
        with col1:
            if promo2:
                st.markdown("""
                    <div style="
                        padding: 10px;
                        background: white;
                        border-radius: 20px;
                        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                    ">
                """, unsafe_allow_html=True)
                st.image(promo2, width='stretch')
                st.markdown("</div>", unsafe_allow_html=True)
                st.caption("<p style='text-align:center; margin-top:10px;'>버컵 실제 활용 모습</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 💡 혁신적인 기술력")
            
            features = [
                ("🛡️", "다공성 단열 구조", "버섯 균사체의 미세 공기층이 열 전도를 차단하여 뜨거운 음료도 안전하게 잡을 수 있습니다."),
                ("💪", "강력한 내구성", "종이보다 질기고 실리콘보다 형태 유지가 뛰어난 고밀도 균사체 구조를 자랑합니다."),
                ("🌱", "100% 생분해", "사용 후 버려지면 45일 이내에 완전히 분해되어 자연의 퇴비로 돌아갑니다."),
                ("🎨", "커스텀 디자인", "브랜드 로고 각인 및 다양한 컵 사이즈에 맞춘 정밀 몰드 제작이 가능합니다.")
            ]
            
            for icon, title, desc in features:
                st.markdown(f"""
                    <div style="
                        padding: 1.2rem;
                        border-radius: 15px;
                        border: 1px solid rgba(46, 125, 50, 0.1);
                        margin-bottom: 1rem;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
                        transition: all 0.3s ease;
                    ">
                        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 1.5rem; margin-right: 10px;">{icon}</span>
                            <span style="font-size: 1.1rem; font-weight: bold; color: #2E7D32;">{title}</span>
                        </div>
                        <p style="font-size: 0.9rem; opacity: 0.8; margin: 0; line-height: 1.5;">{desc}</p>
                    </div>
                """, unsafe_allow_html=True)

    with tab2:
        st.write("")
        st.markdown("<h3 style='text-align: center;'>🛠️ Eco-Friendly Manufacturing</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.7;'>저온, 저에너지 공법으로 탄소 배출을 최소화하는 버컵만의 공정입니다.</p>", unsafe_allow_html=True)
        st.write("")
        
        steps = [
            {"icon": "🚜", "step": "Step 1. 자원 수거", "desc": "지역 버섯 농가에서 버려지는 폐배지를 수거하여 미세하게 분쇄합니다."},
            {"icon": "🧼", "step": "Step 2. 정밀 멸균", "desc": "고온 고압 멸균을 통해 불순물을 제거하고 깨끗한 원료 상태로 만듭니다."},
            {"icon": "🧪", "step": "Step 3. 균사 배양", "desc": "친환경 균사체를 접종한 후, 전용 몰드에서 5~7일간 자연 배양합니다."},
            {"icon": "☀️", "step": "Step 4. 건조 및 완성", "desc": "배양된 제품을 건조하여 성장을 멈추고 내구성을 강화하여 완성합니다."}
        ]
        
        # Vertical Timeline Design using Streamlit Columns for stability
        for i, s in enumerate(steps):
            line_html = f"<div style='width: 2px; height: 50px; background: rgba(46, 125, 50, 0.2); margin: 5px auto;'></div>" if i < len(steps)-1 else ""
            
            c1, c2 = st.columns([0.1, 0.9])
            with c1:
                st.markdown(f"""
                    <div style="display: flex; flex-direction: column; align-items: center;">
                        <div style="
                            width: 35px; height: 35px; background: #2E7D32; color: white; 
                            border-radius: 50%; display: flex; justify-content: center; 
                            align-items: center; font-weight: bold;
                        ">{i+1}</div>
                        {line_html}
                    </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                    <div style="
                        background: rgba(46, 125, 50, 0.03); padding: 1.2rem; 
                        border-radius: 15px; border: 1px solid rgba(46, 125, 50, 0.05);
                        margin-bottom: 10px;
                    ">
                        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 1.2rem; margin-right: 10px;">{s['icon']}</span>
                            <b style="color: #2E7D32;">{s['step']}</b>
                        </div>
                        <p style="font-size: 0.9rem; margin: 0; opacity: 0.8;">{s['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)

    with tab3:
        st.write("")
        st.markdown("<h3 style='text-align: center;'>🔍 전략적 분석 (SWOT)</h3>", unsafe_allow_html=True)
        st.write("")
        
        swot_data = [
            {"title": "Strengths (강점)", "icon": "💪", "content": ["친환경성", "낮은 원가", "우수한 단열성"], "color": "#E8F5E9", "border": "#2E7D32"},
            {"title": "Weaknesses (약점)", "icon": "⚠️", "content": ["대량 생산 공정 초기 단계", "수분 취약성 보완 필요"], "color": "#FFF3E0", "border": "#EF6C00"},
            {"title": "Opportunities (기회)", "icon": "🚀", "content": ["ESG 경영 트렌드", "일회용품 규제 강화"], "color": "#E3F2FD", "border": "#1565C0"},
            {"title": "Threats (위협)", "icon": "🛡️", "content": ["기존 시장 점유 업체의 견제", "소재에 대한 인식 부족"], "color": "#FFEBEE", "border": "#C62828"}
        ]
        
        c1, c2 = st.columns(2)
        for i, item in enumerate(swot_data):
            target_col = c1 if i % 2 == 0 else c2
            with target_col:
                content_html = "".join([f"<li style='font-size: 0.9rem; margin-bottom: 5px;'>{c}</li>" for c in item['content']])
                st.markdown(f"""
                    <div style="
                        background: {item['color']};
                        padding: 1.5rem;
                        border-radius: 15px;
                        border-left: 5px solid {item['border']};
                        margin-bottom: 1rem;
                        height: 180px;
                        color: #333;
                    ">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <span style="font-size: 1.5rem; margin-right: 10px;">{item['icon']}</span>
                            <b style="font-size: 1.1rem;">{item['title']}</b>
                        </div>
                        <ul style="margin: 0; padding-left: 20px;">
                            {content_html}
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

# Business Model Section
elif menu == "비즈니스 모델":
    st.title("📊 Business Model Canvas")
    st.markdown("버컵의 비즈니스 구조를 표준 캔버스 레이아웃으로 확인하세요.")
    st.write("")
    
    # Define the canvas data
    bmc = {
        "KP": {"title": "핵심 파트너", "icon": "🤝", "content": "버섯 폐배지 공급 농가, 컵홀더 양산 공장, B2B 고객사(프랜차이즈 등)"},
        "KA": {"title": "핵심 활동", "icon": "⚙️", "content": "생산 공정 수립, 공장 관리, B2B 영업 및 마케팅, 예비 고객사 샘플 제공"},
        "KR": {"title": "핵심 자원", "icon": "🏗️", "content": "버컵 팀원, 폐버섯 재활용 아이디어 및 브랜드 IP"},
        "VP": {"title": "가치 제안", "icon": "💎", "content": "폐배지 재활용 환경 보호, 종이 사용 감소, 획기적 원가 절감 및 단열 성능"},
        "CR": {"title": "고객 관계", "icon": "❤️", "content": "1:1 전담 응대, SNS 실시간 소통 및 피드백 반영"},
        "CH": {"title": "채널", "icon": "📢", "content": "홍보 홈페이지, SNS 광고, B2B 직접 영업, 펀딩(시장성 검증)"},
        "CS": {"title": "고객 세그먼트", "icon": "👥", "content": "지역 카페/식당, 저가커피 프랜차이즈, 대형마트/편의점"},
        "COST": {"title": "비용 구조", "icon": "💸", "content": "물류비(폐배지 매입), 생산비(공장 가동), 마케팅비, 운영 소모품비"},
        "REV": {"title": "수익원", "icon": "💰", "content": "컵홀더 판매 매출, 기업 맞춤형 OEM 제작 및 협업 수익"}
    }

    # Custom CSS for BMC Layout
    st.markdown("""
        <style>
        .bmc-container {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            grid-template-rows: repeat(2, 250px) auto;
            gap: 10px;
            width: 100%;
        }
        .bmc-box {
            background-color: rgba(46, 125, 50, 0.05);
            border: 1px solid rgba(46, 125, 50, 0.2);
            border-radius: 10px;
            padding: 15px;
            display: flex;
            flex-direction: column;
        }
        .bmc-title {
            font-weight: bold;
            color: #2E7D32;
            font-size: 0.9rem;
            margin-bottom: 10px;
            border-bottom: 1px solid rgba(46, 125, 50, 0.1);
            padding-bottom: 5px;
        }
        .bmc-icon { font-size: 1.5rem; margin-bottom: 5px; }
        .bmc-content { font-size: 0.85rem; line-height: 1.4; opacity: 0.9; }
        
        /* Grid Area Assignments (10-column grid for perfect symmetry) */
        .kp { grid-area: 1 / 1 / 3 / 3; }
        .ka { grid-area: 1 / 3 / 2 / 5; }
        .kr { grid-area: 2 / 3 / 3 / 5; }
        .vp { grid-area: 1 / 5 / 3 / 7; }
        .cr { grid-area: 1 / 7 / 2 / 9; }
        .ch { grid-area: 2 / 7 / 3 / 9; }
        .cs { grid-area: 1 / 9 / 3 / 11; }
        .cost { grid-area: 3 / 1 / 4 / 6; min-height: 120px; }
        .rev { grid-area: 3 / 6 / 4 / 11; min-height: 120px; }
        
        @media (max-width: 1000px) {
            .bmc-container {
                display: flex;
                flex-direction: column;
            }
            .bmc-box { height: auto !important; min-height: 100px; }
        }
        </style>
        
        <div class="bmc-container">
            <div class="bmc-box kp">
                <div class="bmc-title">핵심 파트너</div>
                <div class="bmc-icon">🤝</div>
                <div class="bmc-content">""" + bmc['KP']['content'] + """</div>
            </div>
            <div class="bmc-box ka">
                <div class="bmc-title">핵심 활동</div>
                <div class="bmc-icon">⚙️</div>
                <div class="bmc-content">""" + bmc['KA']['content'] + """</div>
            </div>
            <div class="bmc-box kr">
                <div class="bmc-title">핵심 자원</div>
                <div class="bmc-icon">🏗️</div>
                <div class="bmc-content">""" + bmc['KR']['content'] + """</div>
            </div>
            <div class="bmc-box vp">
                <div class="bmc-title">가치 제안</div>
                <div class="bmc-icon">💎</div>
                <div class="bmc-content">""" + bmc['VP']['content'] + """</div>
            </div>
            <div class="bmc-box cr">
                <div class="bmc-title">고객 관계</div>
                <div class="bmc-icon">❤️</div>
                <div class="bmc-content">""" + bmc['CR']['content'] + """</div>
            </div>
            <div class="bmc-box ch">
                <div class="bmc-title">채널</div>
                <div class="bmc-icon">📢</div>
                <div class="bmc-content">""" + bmc['CH']['content'] + """</div>
            </div>
            <div class="bmc-box cs">
                <div class="bmc-title">고객 세그먼트</div>
                <div class="bmc-icon">👥</div>
                <div class="bmc-content">""" + bmc['CS']['content'] + """</div>
            </div>
            <div class="bmc-box cost">
                <div class="bmc-title">비용 구조</div>
                <div class="bmc-icon">💸</div>
                <div class="bmc-content">""" + bmc['COST']['content'] + """</div>
            </div>
            <div class="bmc-box rev">
                <div class="bmc-title">수익원</div>
                <div class="bmc-icon">💰</div>
                <div class="bmc-content">""" + bmc['REV']['content'] + """</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Q&A Section
elif menu == "Q&A":
    st.title("❓ 자주 묻는 질문")
    st.markdown("버컵에 대해 가장 많이 궁금해하시는 질문들을 모았습니다.")
    st.write("")

    faqs = [
        {
            "q": "🍄 버섯 냄새가 나지 않나요?",
            "a": "전혀 나지 않습니다. 특수 가공 및 건조 과정을 통해 냄새를 완벽히 제거하며, 무향의 깨끗한 상태로 제공됩니다."
        },
        {
            "q": "🔥 뜨거운 음료에도 안전한가요?",
            "a": "네, 버섯 균사체는 천연 단열재 역할을 합니다. 기존 종이 홀더보다 열 차단율이 약 20% 더 우수하여 손을 안전하게 보호합니다."
        },
        {
            "q": "💧 물에 젖으면 흐물거리지 않나요?",
            "a": "천연 왁스 코팅 옵션을 통해 내수성을 확보했습니다. 아이스 음료의 결로 현상에도 충분히 견딜 수 있도록 설계되었습니다."
        },
        {
            "q": "📏 사이즈 조절이 가능한가요?",
            "a": "몰드 제작 방식이므로 고객사가 원하는 모든 사이즈와 형태로 맞춤 제작이 가능합니다. 브랜드 로고 각인도 지원합니다."
        },
        {
            "q": "💰 생산 단가는 어느 정도인가요?",
            "a": "원료비는 거의 0원에 가깝고, 저온/저에너지 공정으로 매우 경제적입니다. 기존 종이 컵홀더 대비 높은 가격 경쟁력을 갖추고 있습니다."
        }
    ]

    for item in faqs:
        st.markdown(f"""
            <div style="
                padding: 1.5rem;
                border-radius: 10px;
                border-left: 5px solid #2E7D32;
                background-color: rgba(128, 128, 128, 0.05);
                margin-bottom: 1.5rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            ">
                <h3 style="margin-top: 0; color: #2E7D32; font-size: 1.2rem;">{item['q']}</h3>
                <p style="margin-bottom: 0; line-height: 1.6;">{item['a']}</p>
            </div>
        """, unsafe_allow_html=True)

# Partnership Section
elif menu == "파트너십":
    st.title("🤝 파트너십 문의")
    st.markdown("버컵과 함께 지속 가능한 미래를 만들어갈 파트너를 찾습니다.")
    st.write("")
    
    # Partnership Types with Cards
    st.markdown("### 🌟 파트너십 유형")
    p1, p2, p3 = st.columns(3)
    
    partners = [
        {"icon": "☕", "title": "카페 점주님", "desc": "차별화된 친환경 이미지를 구축하고 고객에게 특별한 가치를 전달하세요."},
        {"icon": "🚜", "title": "농가 파트너", "desc": "버려지는 폐배지를 새로운 수익원으로 전환하고 자원 순환에 동참하세요."},
        {"icon": "📦", "title": "유통 및 프랜차이즈", "desc": "혁신적인 친환경 제품 라인업을 확보하여 ESG 경영을 실천하세요."}
    ]
    
    cols = [p1, p2, p3]
    for i, p in enumerate(partners):
        with cols[i]:
            st.markdown(f"""
                <div style="
                    background: rgba(46, 125, 50, 0.05);
                    padding: 1.5rem;
                    border-radius: 15px;
                    border: 1px solid rgba(46, 125, 50, 0.1);
                    height: 200px;
                    text-align: center;
                ">
                    <div style="font-size: 2.5rem; margin-bottom: 10px;">{p['icon']}</div>
                    <b style="font-size: 1.1rem; color: #2E7D32;">{p['title']}</b>
                    <p style="font-size: 0.9rem; margin-top: 10px; opacity: 0.8;">{p['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.write("")
    st.divider()
    
    # Contact Form with better UI
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("### 📩 Contact Us")
        st.write("협력 제안이나 제품 문의 등 궁금하신 점을 남겨주시면 담당자가 신속하게 답변해 드립니다.")
        
        st.markdown("""
            <div style="margin-top: 2rem;">
                <p>📍 <b>본사/공장</b>: 경기도 평택시 버컵 생산센터</p>
                <p>📧 <b>이메일</b>: contact@vercup.com</p>
                <p>📞 <b>대표번호</b>: 031-123-4567</p>
                <p>⏰ <b>운영시간</b>: 평일 09:00 - 18:00</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("<h4 style='margin-bottom: 20px;'>문의 양식</h4>", unsafe_allow_html=True)
            
            f1, f2 = st.columns(2)
            with f1:
                name = st.text_input("성함 / 업체명", placeholder="홍길동 / 버컵카페")
            with f2:
                category = st.selectbox("문의 유형", ["샘플 신청", "대량 구매 문의", "농가 협력 제안", "기타 문의"])
                
            email = st.text_input("이메일 주소", placeholder="example@email.com")
            message = st.text_area("상세 내용", placeholder="문의하실 내용을 적어주세요.", height=150)
            
            submitted = st.form_submit_button("🚀 메시지 전송하기")
            if submitted:
                if name and email and message:
                    with st.spinner("메시지를 전송 중입니다..."):
                        success, error_msg = send_email(name, email, category, message)
                        if success:
                            st.balloons()
                            st.success(f"감사합니다, {name}님! 소중한 문의가 정상적으로 접수되었습니다.")
                        else:
                            st.error(f"메일 전송에 실패했습니다: {error_msg}")
                else:
                    st.error("모든 필수 항목(성함, 이메일, 내용)을 입력해 주세요.")

# Footer
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: #666;">
        <p>© 2026 버컵(Vercup) | 경기도 평택시 버컵 생산센터 | contact@vercup.com</p>
    </div>
    """,
    unsafe_allow_html=True
)

